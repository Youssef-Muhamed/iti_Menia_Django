from django.db import models
from category.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    publisher_email = models.EmailField(max_length=255)
    num_of_likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='posts_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_specific_post(self, id):
        return self.objects.get(id=id)

    def get_delete_url(self, id):
        return self.objects.get(id=id)
