from django.db import models
from django.urls import reverse
from django.conf import settings

## Users skal lige undersøges hvordan vi tilføjer fields til standard modellen!!


class Movie(models.Model):
    """Class representing a movie"""

    title = models.CharField(max_length=200)

    date = models.DateTimeField()
    duration = models.IntegerField()
    poster = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None
    )  # Need to look into how this shit works

    ## INFO FOR IMAGEFIELD
    # ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    # Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
    # In addition to the special attributes that are available for FileField, an ImageField also has height and width attributes.
    # To facilitate querying on those attributes, ImageField has the following optional arguments:
    # ImageField.height_field:
    # Name of a model field which will be auto-populated with the height of the image each time the model instance is saved.
    # ImageField.width_field:
    # Name of a model field which will be auto-populated with the width of the image each time the model instance is saved.
    # Requires the Pillow library.
    # ImageField instances are created in your database as varchar columns with a default max length of 100 characters. As with other fields, you can change the #maximum  length using the max_length argument.

    # Metadata
    class Meta:
        ordering = ["date"]

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of movie."""
        return reverse("movie-detail-view", args=[str(self.id)])

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

    # Metadata
    class Meta:
        pass

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse("shift-detail-view", args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.shift_type}, {self.movie.title}, {self.date}"
