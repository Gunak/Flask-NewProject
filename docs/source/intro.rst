Intro
=====

This is a simple command line interface to create a new flask project.
You can create a basic skeleton structure of a simple project that does
a simple "Hello World".

How to Start
************
All you have to do is `flask-skeleton [name]` and this will create a new skeleton directory to start and new project.

.. code-block:: python

    flask-sekelton appName [options]

This will create a directory as such...

.. code-block:: none

    . (current directory)
    |
    +---appName
    |	README.md
    |	LICENSE
    |	setup.py
    |
    +---docs
    |
    +---appName
    |	app.py
    |	__init__.py
    |	+---static
    |	+---template
    |
    +---bin
    |
    +---tests


    