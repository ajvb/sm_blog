from django.conf.urls.defaults import *
from django.views.generic import date_based, list_detail
from django.contrib.auth.views import login, logout

from sm_blog.models import BlogPost

queryset = BlogPost.objects.get_latest_posted_entries()

post_dict = {
    'queryset' : queryset,
    'date_field': 'timestamp',
    'template_object_name': 'post',
}

post_list_dict = {
    'queryset' : queryset,
    'template_name' : 'sm_blog/blog.html',
    'template_object_name': 'post',
    'paginate_by' : 20,
}

urlpatterns = patterns('',
  url(r'^login/$', login, kwargs=dict(template_name='sm_login.html'),
      name='site_login'),
  url(r'^logout/$', logout, kwargs=dict(template_name='sm_logout.html'),
      name='site_logout'),
  url(r'^write/$', 'write_post', name='write_post'),

  url(r'^(?P<slug>[\w-]+)/$',
    date_based.object_detail,
    dict(post_dict, template_name='blog/post.html', slug_field= 'short_url',),
    name='blog_post'),
 
  url(r'^$',
    list_detail.object_list,
    dict(post_list_dict),
    name='blog_list'),
)
