from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ReviewViewSet, StudyViewSet

app_name = 'api'


v1_router = DefaultRouter()
v1_router.register(
    'study',
    StudyViewSet,
    basename='study'
)
v1_router.register(
    'category',
    CategoryViewSet,
    basename='category'
)
v1_router.register(
    r'study/(?P<study_id>\d+)/review',
    ReviewViewSet,
    basename='review'
)
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls))
]
