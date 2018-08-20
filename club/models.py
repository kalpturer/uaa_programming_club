from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, default='')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    summary = models.CharField(max_length=180)
    date = models.DateTimeField(default=timezone.now, blank=True)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
