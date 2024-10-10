# Dependencies
- Node v22.11.1 
- Yarn v1.22.22
- Python v3.12
- Poetry >=1.7.1

# Commands 

## Install:
### Without Makefile
Frontend:
```
yarn install
```
Backend:
```
poetry install --no-root
```
Database:
```
poetry run task aerich-init
poetry run task init-db
poetry run task migrate
```
### Makefile
```
make install-backend
make install-frontend
```
General:
```
make install
```

## Start:
### Without Makefile
```
yarn quasar dev
```
```
poetry run uvicorn server.app:app --reload
```
### Makefile
```
make run-frontend
make run-backend
```
General:
```
make run
```

## Database:
### Without Makefile
Create migrations:
```
poetry run task makemigration
```
Apply migrations:
```
poetry run task migrate
```
Deny migrations:
```
poetry run task downgrade
```
### Makefile
Create migrations:
```
make makemigration
```
Apply migrations:
```
make migrate
```
Deny migrations:
```
make downgrade
```
**General for start**
```
make init-database
```