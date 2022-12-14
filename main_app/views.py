from multiprocessing import context
from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse
# from django.views.generic. import CreateView
from .models import Track, Playlist

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class TrackList(TemplateView):
    template_name= "tracklist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        track = self.request.GET.get("track")
        # If a query exists we will filter by name 
        if track != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["artists"] = Track.objects.filter(artist__icontains=track)
            context["titles"] = Track.objects.filter(title__icontains=track)
            context["stuff"] = f"Searching for {track}"
        else:
            context["artists"] = Track.objects.all()
            context["titles"] = []
            context["Stuff"] = "Trending Artists"
 
        return context

class TrackView(DetailView):
    model = Track
    template_name="trackview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

class TrackCreate(CreateView):
    model = Track
    fields = ['title', 'artist', 'image', 'duration', 'link', 'lyrics']
    template_name= 'createtrack.html'

    def get_success_url(self):
        return reverse('new_track', kwargs={'pk': self.object.pk})

class NewTrack(DetailView):
    model = Track
    template_name="newtrack.html"

class NewTrackView(TemplateView):
    template_name="submitted.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context["newtracks"] = NewTrack
        return context

class LikedTracks(TemplateView):
    template_name = 'liked_tracks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playlists'] = Playlist.objects.all()
        return context        

class PlaylistTrackAssoc(View):

    def get(self, request, pk, track_pk):

        assoc = request.GET.get("assoc")
        
        if assoc == "remove":

            Playlist.objects.get(pk=pk).tracks.remove(track_pk)
        if assoc == 'add':

            Playlist.objects.get(pk=pk).tracks.add(track_pk)
        return redirect("playlists")