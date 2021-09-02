# flask-stock-api

## environment
- [Ubuntu 20.04.2 LTS](https://ubuntu.com)
- [Visual Studio Code 1.59.1](https://code.visualstudio.com/)
- [Python 3.7.11](https://www.python.org/)
- [Flask 2.0.1](https://flask.palletsprojects.com/en/1.1.x/)

## environment variable

```shell
$ export FLASK_APP=main.py
$ export FLASK_CONFIG=development
```

## command

```shell
# run server
$ flask run

# open shell
$ flask shell
```

## database migration

```shell
# init
$ flask db init

# make migration
$ flask db migrate -m "initial migration"

# migrate
$ flask db upgrade
$ flask db downgrade
$ flask db stamp
```
