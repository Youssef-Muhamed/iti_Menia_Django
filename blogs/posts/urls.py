from django.contrib import admin
from django.urls import path
from posts.views import (welcome, say_hello, say_hello_without_name, index,
                         list_users, post_detail,delete_post,create_post,update_post,)
from posts.classViews import PostView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('hello/<int:id>', say_hello, name='hello'),
    path('hello_without_name/', say_hello_without_name, name='hello_without_name'),
    path('posts/', index, name='Postindex'),
    # path('posts/', PostView.as_view(), name='Postindex'),
    path('users/', list_users, name='list_users'),
    # path('<int:id>/show', post_detail, name='postshow'),
    path('<int:pk>', PostDetailView.as_view(), name='postshow'),
    # path('<int:id>/delete', delete_post, name='postdelete'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='postdelete'),
    path('create/',PostCreateView.as_view(),name='postcreate'),
    # path('<int:id>/update',update_post,name='postupdate')
    path('<int:pk>/update',PostUpdateView.as_view(),name='postupdate')
]
