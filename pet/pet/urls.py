from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import CreateView

from study import views
from study.forms import CustomUserForm

handler404 = 'tools.views.page_not_found'
handler500 = 'tools.views.server_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/logout/',
         views.CustomLogoutView.as_view(),
         name='custom_logout'),
    path('auth/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls', namespace='api')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration.html',
            form_class=CustomUserForm,
            success_url=reverse_lazy('study:list')
        ),
        name='registration'
    ),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('project_tools/', include('tools.urls', namespace='tools')),
    path('', include('study.urls', namespace='study')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
