from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import AnonRateThrottle

from study.models import Category, Study
from study.project_tools import filtered_queryset

from .permissions import AuthorOrReadOnly
from .serializers import CategorySerializer, ReviewSerializer, StudySerializer


class StudyViewSet(viewsets.ModelViewSet):
    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    throttle_classes = (AnonRateThrottle,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return filtered_queryset(
            Category.objects, is_admin=self.request.user.is_staff
        )


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        return Study.objects.get(id=self.kwargs['study_id']).reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            study=Study.objects.get(id=self.kwargs['study_id'])
        )
