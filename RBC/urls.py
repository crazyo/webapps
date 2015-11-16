from django.conf.urls import patterns, url

from RBC import views

urlpatterns = patterns('',
    url(r'^flot', views.flot, name='flot'),
    url(r'', views.index, name='index'),
)
