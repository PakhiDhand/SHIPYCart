from django.contrib import admin
from django.urls import path
from home.views import home, about

urlpatterns = [ 
    path("", home, name="shipy-home"),
    path("about", about, name="shipy-about")
]
