from django.conf.urls import url
from . import views

app_name = 'model_creation'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
