from rest_framework import serializers
from posts.models import Post
from posts.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField()
#     publisher_email = serializers.EmailField()
#     version = serializers.IntegerField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)
#     # category = CategorySerializer(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.publisher_email = validated_data.get('publisher_email', instance.publisher_email)
#         instance.version = validated_data.get('version', instance.version)
#
#         instance.category_id = validated_data.get('category', instance.category)
#         instance.save()
#         return instance

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        fields.__add__('category')
