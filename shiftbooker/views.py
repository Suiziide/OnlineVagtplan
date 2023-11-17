from django.shortcuts import get_object_or_404, redirect
from .models import Shift, Movie, Volunteer
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """Index site of the booking system"""
    context = {
        "news": "This is a placeholder for a news object.",
        "movies": sorted(Movie.objects.all(), key=lambda x: x.title),
        "users": User.objects.all(),
    }
    return render(request, "index.html", context=context)


@login_required
def sign_up_for_shift(request, shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    shift.user = request.user  # Assuming 'user' is a ForeignKey in 'Shift' model
    shift.save()

    # Redirect to a success page or back to the same page
    return redirect("some-view-name")


class MovieListView(generic.ListView):
    model = Movie


class MovieDetailView(generic.DetailView):
    model = Movie


class VolunteerListView(generic.ListView):
    model = Volunteer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shifts"] = Shift.objects.all()
        return context


class ShiftDetailView(generic.DetailView):
    model = Shift
