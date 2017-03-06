from django.conf.urls import url
from main.views import MainPageView, main_view


app_name = 'main'

urlpatterns = [
    # url(r'^$', MainPageView.as_view, name='main'),
    url(r'^$', main_view, name='main'),
]
