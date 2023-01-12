from django.contrib import admin
from django.urls import path
from . import views
from home import urls

urlpatterns = [
    path('', views.product,name="productpage"),
    path('cmt/',views.Cmt,name="commentpage"),
     path("search/",views.search,name="searchpage"),
    path("auto/",views.autosearch,name="autopage"),
]
