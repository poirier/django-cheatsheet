Databases
=========

Performance
-----------

From Django 1.6 on, always add `CONN_MAX_AGE` to database settings
to enable persistent connections. `300` is a good starting
value (5 minutes).  `None` will keep them open indefinitely.

Postgresql
----------

MySQL
-----

Ubuntu: need to install (to use MySQL with Django)::

   sudo apt-get install mysql-client mysql-server libmysqlclient-dev

Django::

   pip install MySQL-python

   DATABASES['default'] = {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'dbname',
      'USER': 'username',
      'CONN_MAX_AGE': 300,
   }
