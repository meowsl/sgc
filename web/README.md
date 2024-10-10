# Dependencies
- Node v22.11.1 
- Yarn v1.22.22
- Python v3.12
- Poetry >=1.7.1

# Commands 

## Install:
### Without Makefile
```
yarn install
```
```
poetry install --no-root
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