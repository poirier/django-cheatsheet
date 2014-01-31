Settings
========

Generate a secret key::

    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)

(https://github.com/django/django/blob/master/django/core/management/commands/startproject.py#L26)
