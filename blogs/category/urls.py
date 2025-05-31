
from django.contrib import admin
from django.urls import path
from category.views import cat_index
urlpatterns = [
    path('',cat_index,name='indexCategory'),
]
