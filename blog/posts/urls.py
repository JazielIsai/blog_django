
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import home_page_view, post_create_view, post_list_view, post_update_view, post_complete_view

app_name = 'posts'
urlpatterns = [
    path('', home_page_view, name='list_public'),
    path('mi-lista/', post_list_view, name='list_private'),
    path('crear/', post_create_view, name='create'),
    path('editar/<int:pk>/', post_update_view, name='edit'),
    path('view/<int:pk>/', post_complete_view, name='view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
