from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.addition_list),
]