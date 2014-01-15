=======
Testing
=======

    self.assertEqual(a, b, msg=None)


    rsp = self.client.get(url, [follow=True])
    rsp = self.client.post(url, data, [follow=True])

    rsp.content is a byte string
    rsp['HeaderName']
    rsp.context['template_var']

    assert self.client.login(**login_parms)
  . login(email='foo@example.com', password='cleartextpassword')
