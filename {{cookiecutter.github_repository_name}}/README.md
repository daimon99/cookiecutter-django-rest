#{{cookiecutter.github_repository_name}}

{{cookiecutter.description}}.

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
bin/install
cp .env.sample .env
```
Create the database:

```bash
createdb {{cookiecutter.app_name}}
```
Initialize the git repository

```
git init
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.git
```

Migrate the database and create a superuser:
```bash
python {{cookiecutter.app_name}}/manage.py migrate
python {{cookiecutter.app_name}}/manage.py createsuperuser
```

Run the development server:
```bash
bin/start
```