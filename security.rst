.. _security:

Security
========

SSL
---

SEE ALSO :ref:`nginx` and
`Django docs on SSL and https <https://docs.djangoproject.com/en/1.7/topics/security/#ssl-https>`_.

Basically, make sure nginx is setting X-Forwarded-Proto, then add to settings::

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
