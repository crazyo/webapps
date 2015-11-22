from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feed, name="feed"),
    url(r'^raw/', views.raw_feed, name="raw_feed"),
]
