# Feature Request Application README
[![Build Status][travis-image]][travis-url]
##Technology stack
- PostgreSQL
- Python 2.x
- Flask
- SQLAlchemy
- AngularJs
- Docker Machine(Deployment)

## Installation

```
# Step 1: install virtualenv
> pip install virtualenv

# Step 2: Initialize virtualenv
> virtualenv <name-optional>

# Step 3: Activate virtualenv
> source bin/activate

# Step 4: Setup project
> python setup.py install
# Step 5: Install node packages(make sure you have higer node version>4)
> npm install
# Step 6: Build css and js file
> npm run build && npm start
``` 
## Creating the database
The application uses postgres as the database driver. Make sure that you've got postgres installed on your system before you attempt any of the following steps.
```
# Step 1: access the postgres system user
> sudo su postgres

# Step 2: enter the database
> psql

# Step 3: create features database user
postgres=# create role features with login;

# Step 4: create features database
postgres=# create database features with encoding 'utf-8';

# Step 5: grant permissions to features user on features database
postgres=# grant all privileges on database features to features;

# Step 7: grant permissions to features tables to features user on features database (be sure to do this with the features database selected)
postgres=# \c features
postgres=# grant all privileges on all tables in schema public to features;
```

## Setup database and initial values in database
```
# Step 1: Change config for postgres sql
> vi feature_request/config/default.yml
# Step 2: Migrate all database
> python manage.py db upgrade
# Step 3: Inorder to have some intial values in db(optional)
> python manage.py add
```
## Run

- To run flask server
```
    python manage.py runserver
```

- To run test cases and coverage
```
    python tests.py test
    python tests.py coverage
    npm run test
```

[travis-image]: https://travis-ci.org/arpit2438735/feature-request.svg?branch=master
[travis-url]: https://travis-ci.org/arpit2438735/feature-request