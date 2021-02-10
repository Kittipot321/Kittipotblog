from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import ListTweet,Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class AddTweetForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ListTweet
        fields = ['title','content']
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea,label='Comment')
    class Meta:
        model = Comment
        fields = ['content']