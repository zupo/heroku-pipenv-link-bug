# heroku-pipenv-link-bug

Example app to showcase the bug reported on https://github.com/heroku/heroku-buildpack-python/issues/687


# Steps to recreate

1. Create a new directory and `cd` into it.
2. Copy over the `setup.py` file.
2. Copy over the `src/pipenvbug/__init__.py` file.
4. `pipenv install -e .`
5. `pipenv install pyramid`
6. `pipenv install gunicorn`
