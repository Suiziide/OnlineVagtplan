from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.MovieListView.as_view(), name="movies"),
    path("movie/<int:pk>", views.MovieDetailView.as_view(), name="movie-detail"),
    path("volunteers/", views.VolunteerListView.as_view(), name="volunteers"),
    path("shift/<int:pk>", views.ShiftDetailView.as_view(), name="shift-detail"),
    path(
        "shift/signup/<int:shift_id>/",
        views.sign_up_for_shift,
        name="sign_up_for_shift",
    ),
    path('accounts/', include('django.contrib.auth.urls')),
]
