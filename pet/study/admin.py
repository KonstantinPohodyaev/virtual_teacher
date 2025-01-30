from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, CustomUser, Review, Study

admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    ...


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ...


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...
