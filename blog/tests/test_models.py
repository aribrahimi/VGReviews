from django.test import TestCase
from blog.models import Post, Comment
import datetime


class TestModels(TestCase):

    def setUpPost(self):
        self.post = Post.objects.create(
            title='title 1',
            slug = 'title-1',
            intro= 'i'*20,
            body= 'b'*40,
            date_added= datetime.date.today()
        )

    # def test_title_label
        title_label = self.post._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')
    
    # test_slug_label
        slug_label = self.post._meta.get_field('slug').verbose_name
        self.assertEqual(slug_label, 'slug')

    # test_title_max_length
        title_max_length = self.post._meta.get_field('title').max_length
        self.assertEqual(title_max_length, 150)
    
    # test_slug_max_length
        slug_max_length = self.post._meta.get_field('slug').max_length
        self.assertEqual(slug_max_length, 150)
    
    # test_intro_max_length
        intro_max_length = self.post._meta.get_field('intro').max_length
        self.assertEqual(intro_max_length, 300)
    
    # test_body_max_length
        body_max_length = self.post._meta.get_field('body').max_length
        self.assertEqual(body_max_length, 3000)

    def setUpComment(self):
        self.comment = Comment.objects.create(
            post='title 1',
            name = 'title-1',
            email= 'info@example.com',
            body= 'b'*40,
            date_added= datetime.date.today()
        )

        # test_name_max_length
        title_max_length = self.comment._meta.get_field('name').max_length
        self.assertEqual(title_max_length, 50)
