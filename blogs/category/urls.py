
from django.contrib import admin
from django.urls import path
from posts.views import welcome,say_hello,say_hello_without_name,index,list_users
from category.views import cat_index
urlpatterns = [
    path('',cat_index,name='indexCategory'),
]
