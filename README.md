FlaskAPI
=========
This application provides a basic api with logging and testing. Instructions are below are for mac/linux unless specified.

Setup
----------
Requires python 3.9 to be installed

Setup a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install packages:
    
    $ cd <root repo folder>
    $ pip install -e .

Setup Environment Variables:
    FLASK_ENV is set to production so debug mode will not be on.
    MACOS:
    
    $ export FLASK_APP=basicapi
    $ export FLASK_ENV=production

    
    Windows:
    
    $ SET FLASK_APP=basicapi
    $ SET FLASK_ENV=production


Running
----------------


    $ flask run
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Example requests
----------------

GET request - Accept headers: "application/json"

    $ curl -H "Accept: application/json" http://127.0.0.1:5000/ -v

GET request - without Accept Headers
    curl by default sends `Accept: */*` so we'll need to be explicit with "Accept:" to not send Accept headers

    $ curl  -H "Accept:" http://127.0.0.1:5000/ -v

POST request - Accept headers: "application/json"

    $ curl -X POST -H "Accept: application/json" http://127.0.0.1:5000/ -v

POST request - without Accept Headers

    $ curl -X POST -H "Accept:" http://127.0.0.1:5000/ -v


Logging
-------
By default, when FLASK_ENV is set to development, the app is set to debug mode which includes debug logging.

Custom Debug logging has been added to the route.
Debug mode can be enabled by resetting the env variable and restarting the server: 

    $ export FLASK_ENV=development
    (use SET FLASK_ENV=development for Windows)
    $ flask run

Flask example log
    
    $ [2021-05-13 13:57:53,607] DEBUG in __init__: url: http://127.0.0.1:5000/

Default flask logging can be enabled by removing this line in FlaskAPI/basicapi/__init__.py
It can also be modified to a different log level.

    $ log.setLevel(logging.ERROR)
    
Unit Testing
-------

    $ python -m pytest
