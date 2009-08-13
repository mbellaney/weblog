from django.db import models
from django.contrib.auth.models import User

import datetime

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
	verbose_name_plural = "Categories"

    def get_absolute_url(self):
	return "/categories/%s/" % self.slug

    def __unicode__(self):
        return self.title

STATUS_CHOICES = (
    (1, 'Live'),
    (2, 'Draft'),
)

class Entry(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
