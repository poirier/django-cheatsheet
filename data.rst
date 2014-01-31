====
Data
====

Export/dump data to use as a fixture::

    python manage.py dumpdata --format=yaml --natural app.model >data.yaml

Load it again::

    python manage.py loaddata data.yaml
