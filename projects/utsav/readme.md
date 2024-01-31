# Notes
## Installing Postgresql
### Windows
Pretty much next -> next -> next and install and make sure you remember the password. Then you can use ``psql`` as is. There is no difference between accessing ``postgres`` user or any other user. Just do ``psql -U postgres``. Default port is ``5432`` unless changed.
### Ubuntu
Just do ``sudo apt-get install postgresql`` to install

Unlike Windows, to access ``postgres`` user in ``psql`` command line client, one needs to do ``sudo -u postgres psql``. Root user (or user with sudo) can do anything in the system anyways so there isnt much benefit to setting a password to ``postgres`` database user in Linux.

In order to connect to any other user with ``psql`` command line client, one needs to also supply ``-h localhost``. That means, to connect to the user ``django`` with ``psql`` the command is ``psql -U django -h localhost``. Default port is ``5432`` unless changed.

## Postgres users and setup
There are very few reasons to use ``postgres`` user so it is necessary to create a new user. In my case, I have a user named ``django`` with password ``password`` that has ``createdb`` permission. This permission is necessary to be able to create new database for new projects. To achieve this, log in to ``postgres`` user or any other super user and run the following SQL statements:
```SQL
CREATE ROLE django WITH LOGIN PASSWORD 'password'; -- Create a new user
CREATE DATABASE django WITH OWNER django; -- Sets a default database for django user
ALTER USER django CREATEDB; -- Allows django user to create new databases
```

Now everytime a new project is created, one can simply log in to the ``django`` user by ``psql -U django -h localhost`` and create the necessary database such as
```SQL
CREATE DATABASE newproject;
```
## Django and Postgres
* Install ``psycopg`` with ``pip install psycopg`` along with django.
* Create a new database using ``psql`` as described above
* Change DATABASES section in project's ``settings.py`` like
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Name of the database',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
* Dont forget to migrate
