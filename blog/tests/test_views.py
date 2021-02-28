from django.test import TestCase , Client
from django.urls import reverse
from blog.models import Post
import datetime
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('frontpage')
        self.detail_url = reverse('post_detail', args=['title-1'])
        self.Post1 = Post.objects.create(
            title='title 1',
            slug = 'title-1',
            intro= 'intro 1',
            body= 'text1',
            date_added= datetime.date.today()
        )

    def test_post_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/frontpage.html')

    def test_post_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/post_detail.html')