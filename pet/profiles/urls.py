from django.urls import path

from .views import ProfileDetailView, ProfileListView

app_name = 'profiles'


urlpatterns = [
    path('list/',
         ProfileListView.as_view(),
         name='list'),
    path('detail/<slug:username>/',
         ProfileDetailView.as_view(),
         name='detail')
]
