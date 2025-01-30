from rest_framework import serializers

from study.models import Category, Review, Study

from .validators import mark_validator


class StudySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Study
        fields = '__all__'
        read_only_fields = ['created', 'edit']


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    study = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate_mark(self, mark):
        return mark_validator(mark)
