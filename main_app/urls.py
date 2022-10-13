from django.urls import path

from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('tracks/', views.TrackList.as_view(), name='track_list'),
    path('track_create/', views.TrackCreate.as_view(), name='create_track'),
    path('playlists/<int:pk>/tracks/<int:track_pk>/', views.LikedTracks.as_view(), name='liked_tracks'),
    path('createtrack/', views.TrackCreate.as_view(), name='create_track'),
    path('tracks/<int:pk>/', views.TrackView.as_view(), name='view_track'),
    path('tracks/<int:pk>/tracks/new', views.NewTrack.as_view(), name='new_track'),
    path('submitted/', views.NewTrackView.as_view(), name='submitted'),
 
]
