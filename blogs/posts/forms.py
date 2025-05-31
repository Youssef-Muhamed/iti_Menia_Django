from django import forms
from .models import Post
from category.models import Category
# class PostForm(forms.Form):
#
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)
#     publisher_email = forms.EmailField()
#     num_of_likes = forms.IntegerField()
#     image = forms.ImageField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'content', 'publisher_email', 'num_of_likes', 'image', 'category']
        fields = '__all__'