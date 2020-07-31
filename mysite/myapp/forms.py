#Login form is a reference to a youtube django tutorial
#at url https://www.youtube.com/watch?v=drMr9B3ZcPI
from django import forms
from . import models
class UserInfoForm(forms.Form):
    username = forms.CharField(
        label ='Username',
        required=True,
        max_length=240,
    )
    userpassword = forms.CharField(
        label = 'Password',
        required=True,
        max_length=240,
    )
    email = forms.EmailField(
        label = 'Email',
        required=True,
        max_length=240,
    )
    def save(self):
        info_instance = models.UserInfoModel(
        username = self.cleaned_data["username"],
        userpassword = self.cleaned_data["userpassword"],
        email = self.cleaned_data["email"]
        )
        info_instance.save()

class PostForm(forms.Form):
    content = forms.CharField(
    label = 'Post whatever you like',
    required = True,
    widget=forms.Textarea(attrs={'rows': 1, 'cols': 85}), max_length=160
    )
    image = forms.FileField(required=False)
    def save(self):
        postInstance = models.PostModel(
        content = self.cleaned_data["content"],
        image = self.cleaned_data["image"]
        )
        postInstance.save()

    # country = forms.CharField(widget=forms.HiddenInput())


class DeleteUserForm(forms.Form):
    username = forms.CharField(
    label = 'Username',
    required=True,
    max_length=240,
    )
    def getUsername(self):
        return self.username
