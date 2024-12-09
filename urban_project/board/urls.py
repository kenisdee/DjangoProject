from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('advertisement/<int:pk>/edit/', views.edit_advertisement, name='edit_advertisement'),
    path('advertisement/<int:pk>/delete/', views.delete_advertisement, name='delete_advertisement'),
    path('advertisement/<int:pk>/like/', views.like_advertisement, name='like_advertisement'),
    path('advertisement/<int:pk>/dislike/', views.dislike_advertisement, name='dislike_advertisement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
