from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.sitemaps import ping_google
#from django.utils.translation import ugettext as _ 
#from django import forms

import datetime
#import os

class BlogManager(models.Manager):
    def get_latest_posted_entries(self):
        return super(BlogManager, self).get_query_set()

class BlogPost(models.Model):
    title       = models.CharField(max_length=75)
    body        = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    short_url   = models.SlugField(max_length=40)

    objects = BlogManager()

    class Meta:
        ordering = ['-timestamp']
    
    def save(self):
        super(BlogPost, self).save()
        try:
            ping_google()
        except Exception:
            pass

    def absolute_url(self):
        return ('blog_post', (self.short_url))

    def __unicode__(self):
        return '%s' % self.title
