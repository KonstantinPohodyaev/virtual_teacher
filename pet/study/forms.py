from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Category, CustomUser, Document, Review, Study


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        exclude = ['author']


class CategoryForm(forms.ModelForm):
    class Meta:
        exclude = ['author']
        model = Category


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['author', 'study', 'edited']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
