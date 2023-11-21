from django.shortcuts import get_object_or_404, redirect
from .models import Shift, Movie
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
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
    return render(request, "index.html", context)


@login_required
def sign_up_for_shift(request, shift_id):
    # Retrieve the shift object from the database
    shift = get_object_or_404(Shift, pk=shift_id)

    if request.method == "POST":
        # Handle the POST request to sign up for the shift
        selected_user_id = request.POST.get("selected_user")
        if selected_user_id:
            # Assign the selected user to the shift (assuming 'user' is a ForeignKey in 'Shift' model)
            user = get_user_model().objects.get(id=selected_user_id)
            shift.user = user
            shift.save()
            return redirect(
                "movie-detail", pk=shift.movie.id
            )  # Replace with your actual URL pattern name for shift details

    # Handle the GET request to display the form
    user_list = (
        get_user_model().objects.all()
    )  # You can modify this to get the list of available users
    return render(
        request,
        "shiftbooker/shift_detail.html",
        {"shift": shift, "user_list": user_list},
    )


@login_required
@permission_required("shiftbooker.can_view_users_shifts")
def remove_user_from_shift(request, shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    shift.user = None  # Assuming 'user' is a ForeignKey in 'Shift' model
    shift.save()

    # Redirect to a success page or back to the same page
    return redirect(shift.movie.get_absolute_url())


class MovieListView(LoginRequiredMixin, generic.ListView):
    model = Movie


class MovieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["avail_shifts"] = self.get_object().shift_set.filter(user=None)
        return context


class VolunteerListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    permission_required = "shiftbooker.can_view_users_shifts"
    model = get_user_model()

    template_name = "shiftbooker/volunteer_list.html"

    def get_queryset(self):
        queryset = get_user_model().objects.filter(groups__name="volunteer")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shifts"] = Shift.objects.all()
        return context


class VolunteerDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "shiftbooker/volunteer_detail.html"
    model = get_user_model()
    context_object_name = "volunteer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shift_list"] = Shift.objects.all()
        return context


class ShiftDetailView(LoginRequiredMixin, generic.DetailView):
    model = Shift

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_list"] = get_user_model().objects.all()
        return context
