from django.conf.urls import url
from django.urls.conf import path
from django.urls.resolvers import URLPattern
from sdsApp import views

urlpatterns = [

    path('Allrecords',views.Allrecords,name="Allrecords"),
    url(r'^records',views.SDSApi.as_view())
    
]
