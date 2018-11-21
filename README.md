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


Reflects
--------

To be honest I had not used either Flask/KnockoutJS or even nginx prior to this project,
just your recruiting approach was quite interesting so I decided to invest my time in.
Indeed it was a great opportunity for learning, I managed to walk through some tutorials and
documentations to at least satisfy the business requirements. I also tried to 
incorporate the testing part but encountered some issues along the way, then decided
it was too time-consuming and moved on. All in all it was an enjoyable ride, thanks
for designing this `test chamber`.

