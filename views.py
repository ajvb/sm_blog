from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import list_detail

from sm_blog_site.sm_blog.models import *
from sm_blog_site.sm_blog.model_forms import *


@login_required
def write(request, short_url, template_name="sm_blog/write.html"):
    if request.method == "POST":
        blog_form = BlogPostForm(request.POST)
        if blog_form.is_valid():
            new_blog_post = blog_form.save()
            return HttpResponseRedirect('/')
    else:
        blog_form = BlogPostForm()

    return render(request, 'sm_blog/post.html',{'form':form})

#def blog_post(request, short_url):

def blog_list(requesti, queryset=None, paginate_by=None, template_name=None
              template_object_name=None):
    queryset.order_by('-timestamp')
    return list_detail.object_list(request, queryset, paginate_by=paginate_by
                                   template_name=template_name,
                                   template_object_name=template_object_name)
