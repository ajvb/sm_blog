#from django.db import models
#from django.contrib.auth.models import User
#from django.contrib import admin
from django import forms
from django.conf import settings
from sm_blog.models import *
import datetime

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'body',
        )
