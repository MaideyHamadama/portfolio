from django.conf.urls import url
from . import views

app_name = 'portfolios'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success$', views.mail, name='mail'),
]