from django.shortcuts import render

# Create your views here.
def cat_index(request):
    return render(request, 'category/index.html')