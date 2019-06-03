from django import forms
# from app.models import Snippet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class SnippetCreationForm(UserCreationForm):
#     id = forms.CharField(primary_key=True, max_length=19, default=url_shortner, editable=False)
#     owner = forms.ChoiceField(User, on_delete=models.CASCADE)
#     title = forms.CharField(max_length=50, default="Untitled")
#     content = forms.TextField()
#     creation_date = forms.DateTimeField(auto_now_add=True)
#     expiration_date = forms.DateTimeField(null=True, blank=True)
#     exposure_status = forms.BooleanField()
    
#     class Meta:
#         model = Snippet
#         fields = ['id', 'owner', 'title', 'content', 
#         'creation_date', 'expiration_date', 'exposure_status']