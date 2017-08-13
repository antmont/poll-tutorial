from django.conf.urls import url

from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.post_list, name='post_list'),
    # /blog/post/5/
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # /blog/post/new/
    url(r'^post/new/$', views.post_new, name='post_new'),
    # /blog/post/5/edit/
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
