from django import forms

from .models import Post, Comment

from blog.models import CategoryModel
from django.contrib.auth.models import User


FRUIT_CHOICES= [('Faculty','FACULTY'),('Office','OFFICE'),('Committee','COMMITTEE'),('Campus','CAMPUS'),]


class PostForm(forms.ModelForm):

    

    class Meta:
        model = Post
        fields = ('typez','title','text','favorite_fruit')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'author': forms.TextInput(attrs={'readonly':'readonly'}),
            'favorite_fruit': forms.Select(choices=FRUIT_CHOICES),
        }
        exclude = ["username"]

        labels = {

        'favorite_fruit' : 'What is category of your request?',
        'typez' : 'Type',
        }





class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text'}),
        }



#mine


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')

        help_texts = {
            'username': None,
        }


# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('Name','Roll_Number')


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['color']