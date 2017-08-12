from django.conf.urls import url

from . import views

urlpatterns = [
    # /blog/
    url(r'^$', views.post_list, name='post_list'),
]
