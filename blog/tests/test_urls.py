from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import frontpage, post_detail

class TestUrls(SimpleTestCase):

    def test_frontpage_url_resolves(self):
        url = reverse('frontpage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, frontpage)

    def test_detail_url_resolves(self):
        url = reverse('post_detail',args=['slug'])
        self.assertEquals(resolve(url).func, post_detail)

