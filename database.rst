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
