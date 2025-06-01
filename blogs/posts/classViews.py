from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Post
from .forms import PostForm
# Create your views here.
from  category.models import Category
# class PostView(View):
#     def get(self,request):
#         # post_get = Post.get_specific_post(Post,id=id)
#         posts = Post.objects.all()
#         return render(request, 'posts/index.html',context={'posts':posts})
#
#
# class PostCreateView(View):
#     def get(self,request):
#         forms = PostForm()
#         return render(request, 'posts/create.html',context={'forms':forms})
#     def post(self,request):
#         forms = PostForm(request.POST, request.FILES)
#         if forms.is_valid():
#             forms.save()
#             return redirect('Postindex')
#         return render(request, 'posts/create.html')

class PostView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostForm
    success_url = '/posts/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/postDetail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    form_class = PostForm
    success_url = '/posts/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = '/posts/'