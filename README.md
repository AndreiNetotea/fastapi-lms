## Requirements

### Virtual environment

- To run this project is better to a have a virtual environment. To achieve that you can create one using `python` native virtual env manager:
    - `python -m venv fastatpi` -  create a virtual environment `fastatpi`.
    - `source fastatpi/bin/activate` - activate `fastatpi` virtual env.
    - `deactivate` - exits from virtual environment.

- You will need `poetry` to run this project, you can do that using `pip`, `pip install poetry`

## Install the requirement
- After you created your virtual environment and `poetry` is installed you should install the dependencies of the project using:
    - `poetry install`
    - `poetry add package-name` to install a new package (eg. `poetry add sqlalchemy`).


## Start the application
- `uvicorn main:app --reload` to start the application.

## Swagger
- After you start the application you can find swagger on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Migrations
- For the migrations we are using `alembic`, here are some useful commands:
    - `alembic init alembic` - init alembic inside your project
    - `alembic revision --autogenerate` - autogenerate migration files.
    - `alembic upgrade head` - run migrations.
    - `alembic downgrade base` - undo migrations.



## Recommendations

- You can also can install `pyenv` for multiple python versions.
    - If you have `pyenv` installed you can create a new virtual env using this command `pyenv virtualenv myvirtualenv`
    - list virtual envs `pyenv virtualenvs`
    - `pyenv activate myvirtualenv` activate `myvirtualenv`
    - `pyenv deactivate`
    - `pyenv uninstall my-virtual-env` and `pyenv virtualenv-delete my-virtual-env` for deletion.

