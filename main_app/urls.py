from django.urls import path

from main_app.models import Track
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('browsesongs/', views.TrackList.as_view(), name='track_list'),
    path('createtrack/', views.TrackCreate.as_view(), name='create_track'),
    path('viewtrack/<int:pk>/', views.TrackView.as_view(), name='view_track'),
    path('newtrack/<int:pk>/', views.NewTrack.as_view(), name='new_track'),
    path('submitted/', views.NewTrackView.as_view(), name='submitted'),
 
]
