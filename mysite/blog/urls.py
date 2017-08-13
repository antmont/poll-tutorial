from django.conf.urls import url

from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.post_list, name='post_list'),
    # /blog/post/5/
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
