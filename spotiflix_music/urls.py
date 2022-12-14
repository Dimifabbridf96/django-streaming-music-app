"""spotiflix_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from streaming_music.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),  
    path('add1', addSong, name='add1'),  
    path('add', addAlbum, name='add'),
    path('edit/<int:album_id>', editAlbum, name='edit'),
    path('edit1/<int:song_id>', editSong, name='edit1'),
    path('<int:id>/delete/<int:song_id>', removeSong, name='delete_song'),
    path('<int:id>/remove/<int:album_id>', deleteAlbum, name='delete_album'),
    path('', include('streaming_music.urls'), name='music_urls'),
    path('accounts/', include('allauth.urls')),    
]
