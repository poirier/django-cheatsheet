Settings
========

Generate a secret key:

.. code-block:: python

    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)

(https://github.com/django/django/blob/master/django/core/management/commands/startproject.py#L26)



Log errors to console in local.py:

.. code-block:: python

    LOGGING.setdefault('formatters', {})
    LOGGING['formatters']['verbose'] = {
        'format': '[%(name)s] Message "%(message)s" from %(pathname)s:%(lineno)d in %(funcName)s'
    }
    LOGGING['handlers']['console'] = {
        'class': 'logging.StreamHandler',
        'formatter': 'verbose',
        'level': 'ERROR',
    }
    LOGGING['loggers']['django'] = {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
    }
