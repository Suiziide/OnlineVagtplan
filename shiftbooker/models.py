from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


## Users skal lige undersøges hvordan vi tilføjer fields til standard modellen!! Det har vi gjort.
## https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#auth-custom-user ?


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)


class User(AbstractUser):
    """Class representing a user"""

    registered = models.DateField(
        ("Registration Date"), auto_now=False, auto_now_add=True
    )
    phone = models.CharField(max_length=100)
    shifts_taken = models.IntegerField("Number of shifts taken", default=0)
    objects = CustomUserManager()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        permissions = (("can_view_users_shifts", "Can view users and shifts"),)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of movie."""
        return reverse("volunteer-detail", args=[str(self.id)])


class Movie(models.Model):
    """Class representing a movie"""

    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    duration = models.IntegerField()
    poster = models.ImageField(
        upload_to="", height_field=None, width_field=None, max_length=None, blank=True
    )

    # Metadata
    class Meta:
        ordering = ["date"]

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of movie."""
        return reverse("movie-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title


class Shift(models.Model):
    """Class representing a shift"""

    SHIFT_TYPES = (
        ("m", "Maintenance"),
        ("s", "Shop"),
        ("c", "Cleaning"),
        ("o", "A/V Operations"),
        ("p", "Event Planning"),
    )

    shift_type = models.CharField(
        max_length=1,
        choices=SHIFT_TYPES,
    )
    date = models.DateTimeField()
    duration = models.IntegerField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    # user = models.ForeignKey(
    #    "Volunteer", on_delete=models.SET_NULL, null=True, blank=True
    # )

    # Metadata
    class Meta:
        pass

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse("shift-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.movie.title}, {self.date}"


# class Volunteer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     registered = models.DateField(
#         ("Registration Date"), auto_now=False, auto_now_add=True
#     )
#     phone = models.CharField(max_length=100)
#     shifts_taken = models.IntegerField("Number of shifts taken", default=0)

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.user.username
