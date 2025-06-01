from django.contrib import admin
from django.urls import path, include
# from posts.api.view import list_all_posts, post_detail
from posts.api.view import PostList,PostList,PostRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('posts/', PostList.as_view(), name='list_all_posts'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail')
]
