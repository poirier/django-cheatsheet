Email
=====

https://docs.djangoproject.com/en/1.6/topics/email/

API
---

Send one email::

    send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None)¶


Console email handler
---------------------

For development::

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
