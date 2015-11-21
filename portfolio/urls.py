from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.fixed_income, name="portfolio"),

]