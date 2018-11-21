Fitcha - A neat platform for feature requests
======

A simple application written in Flask and KnockoutJS for showing, adding and
deleting _feature requests_.


Install
-------

Create a virtualenv and activate it

    python3 -m venv venv
    . venv/bin/activate

Install Fitcha

    pip install -e .

Run
---

    # Init database
    python3
    >>> from index import db
    >>> db.create_all()
    >>> exit()
    
    export FLASK_APP=index.py
    export FLASK_ENV=development
    flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

There are no tests included and I am deeply sorry about that.


Deployment
----------

    make deploy
    
The app is hosted [here](http://thaivu.cf). 

