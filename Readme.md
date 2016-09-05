# Feature Request Application README
[![Build Status][travis-image]][travis-url]
##Technology stack
- PostgreSQL
- Python 2.x
- Flask
- SQLAlchemy
- AngularJs

##Installation

```
# Step 1: install virtualenv
> pip install virtualenv

# Step 2: Initialize virtualenv
> virtualenv <name-optional>

# Step 3: Activate virtualenv
> source bin/activate

# Step 4: Setup project
> python setup.py
# Step 5: Install node packages(make sure you have higer node version>4)
> npm install
# Step 6: Build css and js filder
> npm run build && npm start
``` 

##Run

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