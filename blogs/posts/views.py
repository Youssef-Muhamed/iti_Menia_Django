from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound

from .models import Post
from .forms import PostForm
# Create your views here.
from  category.models import Category
def welcome(request):
    return HttpResponse("welcome from django course")

def say_hello(request,id):
    return HttpResponse(f"<p style='color:red;font-size:50px'>hello {id}</p>")

def say_hello_without_name(request):
    return HttpResponse(f"<p style='color:red;font-size:50px'>hello </p>")
# posts = [{
#     'id':1,
#     'title':'first post',
#     'content':'This is the first post'
# },{
#     'id':2,
#     'title':'second post',
#     'content':'This is the second post'
# },{
#     'id':3,
#     'title':'third post',
#     'content':'This is the third post'
# }]
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html',context={'posts':posts})

def list_users(request):
    users = ['Aya','Abo','Arwa','Salma','Alyaa','Abelhameed']
    return render(request, 'posts/users.html',context={'users':users})

def post_detail(request,id):

    post_get = Post.get_specific_post(Post,id=id)

    return render(request, 'posts/postDetail.html',context={'post':post_get})

def delete_post(request,id):
    post_get = Post.get_specific_post(Post,id=id)
    post_get.delete()
    return redirect('Postindex')

def create_post(request):
    if request.method == 'GET':
        category_get = Category.objects.all()
        forms = PostForm()
        return render(request, 'posts/create.html',context={'forms':forms})
    elif request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # publisher_email = request.POST.get('publisher_email')
        # num_of_likes = request.POST.get('num_of_likes')
        #
        # image = request.FILES.get('image') #
        # category = Category.objects.get(id=request.POST.get('category'))
        # Post.objects.create(title=title,
        #                     content=content,
        #                     publisher_email=publisher_email,
        #                     num_of_likes=num_of_likes,
        #                     image=image,
        #                     category=category)

        forms = PostForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('Postindex')
        return render(request, 'posts/create.html')


def update_post(request,id):
    post_get = Post.get_specific_post(Post,id=id)
    if request.method == 'GET':
        forms = PostForm(instance=post_get)
        return render(request, 'posts/update.html',context={'forms':forms})
    elif request.method == 'POST':
        forms = PostForm(request.POST, request.FILES,instance=post_get)
        if forms.is_valid():
            forms.save()
            return redirect('Postindex')
        return render(request, 'posts/update.html')










