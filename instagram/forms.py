from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField

class LikesForm(forms.Form):
    class Meta:
        model = Image
        exclude = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['prof_pic','bio']
        
        
class UploadPicForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ('user','profile')