=======
Testing
=======

.. code-block:: python

    self.assertEqual(a, b, msg=None)


    rsp = self.client.get(url, [follow=True])
    rsp = self.client.post(url, data, [follow=True])

    rsp.content is a byte string
    rsp['HeaderName']
    rsp.context['template_var']

    assert self.client.login(**login_parms)
    login(email='foo@example.com', password='cleartextpassword')



# http://docs.python.org/library/unittest.html
# https://docs.djangoproject.com/en/dev/topics/testing/

.. code-block:: python

from django.test import TestCase
from django.contrib.auth.models import User


class XxxTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', 'test@example.com', 'testpass')

    def test_something(self):
        response = self.client.get(show_timemap)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['lat'], '123.123')
        self.assertEqual(response.context['lon'], '456.456')
        self.assertContains(response, "some text")
        self.assertNotContains(response, "other text")
        self.assertIsNone(val)
        self.assertIsNotNone(val)
        self.assertIn(thing, iterable)  # Python >= 2.7
        self.assertNotIn(thing, iterable)  # Python >= 2.7
