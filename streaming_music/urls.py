from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AlbumList.as_view(), name='home'),
    path('<slug:title>/', views.AlbumView.as_view(), name='albums'),
    path('like/<slug:title>', views.AlbumLike.as_view(), name='albums_like')
]