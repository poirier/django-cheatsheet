====
URLs
====

reverse
=======

Ex::

    from django.core.urlresolvers import reverse

    reverse(viewname='myview',   # remaining args optional
            urlconf=None,
            args=(1, 2),
            kwargs={'pk': foo.pk},
            current_app=None)
