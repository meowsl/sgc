import shutil
import dotenv
import string
import secrets
import os


class EnvGenerator:
    """
    Генерация env файла
    """

    def __init__(self):
        project_root = self.find_project_root(os.getcwd(), ".env.example")
        self.env_example_path = os.path.join(
            project_root, ".env.example"
        )
        self.env_path = os.path.join(project_root, ".env")

    def find_project_root(self, start_path, target_file):
        """
        Динамический поиск директории
        """
        current_path = os.path.abspath(start_path)
        while True:
            if os.path.exists(os.path.join(current_path, target_file)):
                return current_path
            parent_path = os.path.dirname(current_path)
            if parent_path == current_path:
                raise FileNotFoundError(
                    f"{target_file} not found in any parent directory")
            current_path = parent_path

    def generate_key(self, length=64):
        """
        Генерация случайного ключа
        """
        chars = string.ascii_letters + string.digits + '!@%&()-_=+'
        return "".join(secrets.choice(chars) for _ in range(length))

    def create_env(self):
        """
        Создание env файла
        """
        shutil.copy(self.env_example_path, self.env_path)

        dotenv.load_dotenv(self.env_path)
        dotenv.set_key(self.env_path, "SECRET_KEY", self.generate_key())


if __name__ == "__main__":
    generator = EnvGenerator()
    generator.create_env()
