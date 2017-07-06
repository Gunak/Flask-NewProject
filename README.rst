Flask-ProjectManager
====================

This is a command line tool that will create a new Flask application with the ability to create a simple setup or if you are using blueprints.

.. image:: https://travis-ci.org/Gunak/Flask-NewProject.svg?branch=master
    :target: https://travis-ci.org/Gunak/Flask-NewProject

.. image:: https://badge.fury.io/py/Flask-NewProject.svg
    :target: https://badge.fury.io/py/Flask-NewProject


Getting Started
===============

Prerequisites
*************


Installing
**********

    pip install Flask-NewProject

Usage Commands
**************

For a skeleton structure:
    flask-skeleton ProjectName

This will create a simple skeleton structure with app.py created but with no content inside of it.

For a simple structure:
    flask-simple ProjecName

This is the same as the skeleton structure with the addition of basic content in app.py and a test.py in the test directory. You can also run flask-simple right after flask-skeleton and it will add the basic setup into app.py as well.


Running Tests
*************

Testing your new simple-structure
I use nosetests from the project folder and run
    nosetests

There are two built in tests with flask-simple. One the check response code 200 and the other is for Hello World!



Contributing
************

Please contribute if you can. This project is just getting underway, but help is always welcome.


Version Information
*******************
Current version 0.2.1

Authors
*******

Raymond Williams



License
*******

This project is licensed under the MIT License - see the LICENSE file for details
