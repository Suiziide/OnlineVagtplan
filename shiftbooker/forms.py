from django.forms import (
    ModelForm,
    ValidationError,
    DateTimeInput,
    PasswordInput,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from shiftbooker.models import Movie, Shift
from django.contrib.auth import get_user_model


class CreateUserForm(ModelForm):
    def clean(self):
        data = super().clean()
        if not (data["phone"]).isdigit() or len(data["phone"]) != 8:
            raise ValidationError(
                ("Invalid Input - Phone Number Must Consist of 8 Digits")
            )
        return data

    class Meta:
        model = get_user_model()

        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "groups",
            "shifts_taken",
        ]
        widgets = {
            "password": PasswordInput(),
            # "email": EmailInput()
        }


class CreateShowForm(ModelForm):
    def clean(self):
        data = super().clean()  # ???

        # Check if a date is not in the past.
        if data["date"] < timezone.now():
            raise ValidationError(("Invalid Input - date must not be in the past"))

        # Check if duration is positive
        if data["duration"] < 0:
            raise ValidationError(("Invalid Input - duration must non-negative"))

        return data

    class Meta:
        model = Movie
        fields = "__all__"
        labels = {
            "title": _("Title of Movie"),
            "date": _("Date and Time of Showstart"),
            "duration": _("Duration of Show"),
            "poster": _("Image for Movie-Poster (optional)"),
        }
        widgets = {
            "date": DateTimeInput(
                format=("%Y-%m-%dT%H:%M"), attrs={"type": "datetime-local"}
            )
        }


class CreateShiftForm(ModelForm):
    def clean(self):
        data = super().clean()

        # Check if a date is not in the past.
        if data["date"] < timezone.now():
            raise ValidationError(("Invalid Input - date must not be in the past"))

        # Check if duration is positive
        if data["duration"] < 0:
            raise ValidationError(("Invalid Input - duration must non-negative"))

        return data

    class Meta:
        model = Shift
        fields = "__all__"
        widgets = {
            "date": DateTimeInput(
                format=("%Y-%m-%dT%H:%M"), attrs={"type": "datetime-local"}
            )
        }
