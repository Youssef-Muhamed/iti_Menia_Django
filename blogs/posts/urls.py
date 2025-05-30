
from django.contrib import admin
from django.urls import path
from posts.views import welcome,say_hello,say_hello_without_name,index,list_users
urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('hello/<int:id>', say_hello, name='hello'),
    path('hello_without_name/', say_hello_without_name, name='hello_without_name'),
    path('posts/',index,name='Postindex'),
    path('users/',list_users,name='list_users'),
]
