from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('',home,name="home" )
]