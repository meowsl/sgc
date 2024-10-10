install-backend:
	@poetry env use 3.12.0
	@poetry run task env
	@poetry install --no-root

install-frontend:
	@yarn install

.PHONY: run-backend
run-backend:
	@poetry run task run-server

.PHONY: run-frontend
run-frontend:
	@yarn quasar dev

.PHONY: run
run:
	@make -j 2 run-backend run-frontend

.PHONY: install:
install:
	@make -j 2 install-backend install-frontend