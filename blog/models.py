from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    intro = models.TextField(max_length=300)
    body = models.TextField(max_length=3000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    body = models.TextField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']