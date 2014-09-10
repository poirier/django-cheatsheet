.. Django Cheat-sheet documentation master file, created by
   sphinx-quickstart on Tue Jan  7 09:16:01 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Cheat-sheet's documentation!
==============================================

These are just things I always find myself looking up, so I try to
make some notes of the most important parts that I can refer back to.

Contents:

.. toctree::
   :maxdepth: 2

   admin
   celery
   data
   ddt
   email
   forms
   logging
   mysql
   permissions
   queries
   settings
   test
   translation
   urls


Misc to file:

Avoid circular imports::

    from django.db.models import get_model
    MyModel = get_model('applabel', 'mymodelname'.lower())

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

