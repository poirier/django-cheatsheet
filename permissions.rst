===========
Permissions
===========

(Note: this page is about authorization, not authentication.)

Link: https://docs.djangoproject.com/en/1.6/topics/auth/default/#topic-authorization

User objects have two many-to-many fields: groups and user_permissions. User objects can access their related objects in the same way as any other Django model::

    myuser.groups = [group_list]
    myuser.groups.add(group, group, ...)
    myuser.groups.remove(group, group, ...)
    myuser.groups.clear()
    myuser.user_permissions = [permission_list]
    myuser.user_permissions.add(permission, permission, ...)
    myuser.user_permissions.remove(permission, permission, ...)
    myuser.user_permissions.clear()

Assuming you have an application with an app_label foo and a model named Bar, to test for basic permissions you should use:

* add: user.has_perm('foo.add_bar')
* change: user.has_perm('foo.change_bar')
* delete: user.has_perm('foo.delete_bar')

.. NOTE::

    There is no default permission for read access.

The Permission model is rarely accessed directly, but here it is::

    permission = Permission.objects.create(codename='can_publish',
                                           name='Can Publish Posts',  # verbose human-readable name
                                           content_type=content_type)

Permissions are more commonly referred to by a string, of the form "app_label.codename".
E.g., ``if user.has_perm('myapp.codename'):  do something``.

Confusingly, the ``Permission`` model has no ``app_label`` field.
It uses ``content_type__app_label`` for that.

.. WARNING::

    This means all permissions
    need a content type, whether it makes sense for that permission to
    be applied to a particular model or not.

To create a new permission programmatically::

    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.create(codename='can_publish',
                                           name='Can Publish Posts',
                                           content_type=content_type)


Default permissions
-------------------

https://docs.djangoproject.com/en/1.6/topics/auth/default/#default-permissions

For every model in an installed app, Django automatically creates three
permissions: `applabel.add_modelname`, `applabel.change_modelname`, and
`applabel.delete_modelname`, where the modelname is lowercased.

Adding model permissions
------------------------

https://docs.djangoproject.com/en/1.6/ref/models/options/#permissions

You can ask Django to create more permissions for a model::

    class Meta:
        permissions = [
            ('codename', 'verbose name'),
        ]

When the table is created during ``syncdb``, Django will create the additional
Permission objects too.

.. WARNING::

    Such permissions are *only* created when Django creates the model's
    table during ``syncdb``. Adding permissions to the model definition
    later does nothing (unless you drop the table and force Django to
    create it again).

You can programmatically force Django to create additional Permissions
with code like::

    from django.db.models import get_models, get_app
    from django.contrib.auth.management import create_permissions

    apps = set([get_app(model._meta.app_label) for model in get_models()])
    for app in apps:
        create_permissions(app, None, 2)

Checking permissions in templates
---------------------------------

https://docs.djangoproject.com/en/dev/topics/auth/default/#authentication-data-in-templates

    {% if user.is_authenticated %}
    {% if perms.applabel %} {# user has any permissions in app `applabel` #}
    {% if 'applabel' in perms %} {# same as above %}
    {% if perms.applabel.change_thing %} {# user has 'change_thing' permission in app `applabel` #}
    {% if 'applabel.change_thing' in perms %} {# same as above #}
