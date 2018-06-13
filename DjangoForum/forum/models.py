import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_str


DOMAINS = (
    ('FB', 'Football'),
    ('VB', 'Volleyball'),
    ('HB', 'Handball'),
    ('BB', 'Basketball'),
)


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return smart_str(self.pk) + '. ' + self.name


class Topic(models.Model):
    title = models.CharField(max_length=100)
    domain = models.CharField(
        max_length=2,
        choices=DOMAINS,
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return smart_str(self.pk) + '. ' + self.title


class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return smart_str(self.pk) + '. ' + self.text

