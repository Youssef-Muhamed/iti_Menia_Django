from posts.models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from rest_framework.views import APIView
# @csrf_exempt
# def list_all_posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         data = []
#         for post in posts:
#             data.append({
#                 'id':post.id,
#                 'title':post.title,
#                 'content':post.content,
#                 'publisher_email':post.publisher_email,
#                 'created_at':post.created_at,
#                 'updated_at':post.updated_at,
#             })
#         return JsonResponse(data,safe=False)
#
#     if request.method == 'POST':
#         post_data = json.loads(request.body)
#         Post.objects.create(**post_data)
#         return JsonResponse({'message': 'Post created successfully', 'status': 200})
# @csrf_exempt
# def list_all_posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
#
#     if request.method == 'POST':
#         json_data = json.loads(request.body)
#         serializer = PostSerializer(data=json_data)
#         if serializer.is_valid():
#             print("is valid")
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def list_all_posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer