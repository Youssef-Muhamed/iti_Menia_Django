from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("welcome from django course")

def say_hello(request,id):
    return HttpResponse(f"<p style='color:red;font-size:50px'>hello {id}</p>")

def say_hello_without_name(request):
    return HttpResponse(f"<p style='color:red;font-size:50px'>hello </p>")

def index(request):
    posts = [{
        'id':1,
        'title':'first post',
        'content':'This is the first post'
    },{
        'id':2,
        'title':'second post',
        'content':'This is the second post'
    },{
        'id':3,
        'title':'third post',
        'content':'This is the third post'
    }]
    return render(request, 'posts/index.html',context={'posts':posts})

def list_users(request):
    users = ['Aya','Abo','Arwa','Salma','Alyaa','Abelhameed']
    return render(request, 'posts/users.html',context={'users':users})