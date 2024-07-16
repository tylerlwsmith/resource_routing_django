from django.db import models


class BlogPost(models):
    title = models.CharField(max_length=100)
    body = models.TextField()
