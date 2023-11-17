from .models import Shift, Movie
#from django.contrib.auth import User
from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    """Index site of the booking system"""
    context = {
        'news' : "This is a placeholder for a news object.",
        'movies' : sorted(Movie.objects.all(), key=lambda x: x.title)
    }
    return render(request, 'index.html', context=context)


class MovieListView(generic.ListView):
    model = Movie

class MovieDetailView(generic.DetailView):
    model = Movie

#class UserListView(generic.ListView):
    #model = User
    #context_object_name = 'user_list'