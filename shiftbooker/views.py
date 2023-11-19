from django.shortcuts import get_object_or_404, redirect
from .models import Shift, Movie
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model


# Create your views here.
@login_required
def index(request):
    """Index site of the booking system"""
    context = {
        "news": "This is a placeholder for a news object.",
        "movies": sorted(Movie.objects.all(), key=lambda x: x.title),
        "users": get_user_model().objects.all(),
    }
    return render(request, "index.html", context=context)


@login_required
def sign_up_for_shift(request, shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    shift.user = request.user  # Assuming 'user' is a ForeignKey in 'Shift' model
    shift.save()

    # Redirect to a success page or back to the same page
    return redirect("some-view-name")


class MovieListView(LoginRequiredMixin, generic.ListView):
    model = Movie


class MovieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie


class VolunteerListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    permission_required = 'shiftbooker.can_view_users_shifts'
    model = get_user_model()

    template_name = 'shiftbooker/volunteer_list.html'

    def get_queryset(self):
        queryset = get_user_model().objects.filter(groups__name="volunteer")
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shifts"] = Shift.objects.all()
        return context


class ShiftDetailView(LoginRequiredMixin, generic.DetailView):
    model = Shift
