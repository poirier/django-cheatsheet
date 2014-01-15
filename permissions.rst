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

The Permission model is rarely accessed directly.

    permission = Permission.objects.create(codename='can_publish',
                                           name='Can Publish Posts',
                                           content_type=content_type)

