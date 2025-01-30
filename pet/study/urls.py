from django.urls import path

from . import views


app_name = 'study'


urlpatterns = [
     path('',
          views.StudyListView.as_view(),
          name='list'),
    path('study/create/',
         views.StudyCreateView.as_view(),
         name='create'),
    path('study/detail/<int:study_id>/add_documents/',
         views.add_documents_for_study,
         name='download_documents'),
    path('study/detail/<int:study_id>/',
         views.StudyDetailView.as_view(),
         name='detail'),
    path('study/update/<int:study_id>/',
         views.StudyUpdateView.as_view(),
         name='update'),
    path('study/delete/<int:study_id>/',
         views.StudyDeleteView.as_view(),
         name='delete'),
    path('study/<int:study_id>/review/create/',
         views.ReviewCreateView.as_view(),
         name='review_create'),
    path('study/<int:study_id>/review/update/<int:review_id>/',
         views.ReviewUpdateView.as_view(),
         name='review_update'),
    path('study/<int:study_id>/review/delete/<int:review_id>/',
         views.ReviewDeleteView.as_view(),
         name='review_delete'),
    path('category/list/',
         views.CategoryListView.as_view(),
         name='category_list'),
    path('category/create/',
         views.CategoryCreateView.as_view(),
         name='category_create'),
    path('category/detail/<slug:category_slug>/',
         views.CategoryDetailView.as_view(),
         name='category_detail'),
    path('category/update/<slug:category_slug>/',
         views.CategoryUpdateView.as_view(),
         name='category_update'),
    path('category/delete/<slug:category_slug>/',
         views.CategoryDeleteView.as_view(),
         name='category_delete'),
]
