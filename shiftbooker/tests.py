from django.test import TestCase
from django.urls import reverse
from .models import Shift, Movie
from django.contrib.auth import get_user_model


# Create your tests here.
class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("(MovieModelTest)")
        # Set up non-modified objects used by all test methods
        Movie.objects.create(
            title="Test Movie", date="2024-01-01T12:00:00Z", duration=120, poster=None
        )

    def test_get_absolute_url(self):
        movie = Movie.objects.get(id=1)
        expected_url = reverse("movie-detail", args=[str(movie.id)])
        self.assertEqual(movie.get_absolute_url(), expected_url)

    def test_title_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_date_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_duration_label(self):
        movie = Movie.objects.get(id=1)
        field_label = movie._meta.get_field("duration").verbose_name
        self.assertEqual(field_label, "duration")

    def test_title_max_length(self):
        movie = Movie.objects.get(id=1)
        max_length = movie._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_str_method(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(str(movie), movie.title)


class ShiftModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("(ShiftModelTest)")
        # Set up non-modified objects used by all test methods
        movie = Movie.objects.create(
            title="Test Movie",
            date="2023-01-01T12:00:00Z",  # Replace with a valid date and time
            duration=120,
        )
        Shift.objects.create(
            shift_type="m",
            date="2023-01-02T12:00:00Z",  # Replace with a valid date and time
            duration=60,
            movie=movie,
            user=None,  # Assuming this is a nullable field
        )

    def test_get_absolute_url(self):
        shift = Shift.objects.get(id=1)
        expected_url = reverse("shift-detail", args=[str(shift.id)])
        self.assertEqual(shift.get_absolute_url(), expected_url)

    def test_shift_type_label(self):
        shift = Shift.objects.get(id=1)
        field_label = shift._meta.get_field("shift_type").verbose_name
        self.assertEqual(field_label, "shift type")

    def test_date_label(self):
        shift = Shift.objects.get(id=1)
        field_label = shift._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_duration_label(self):
        shift = Shift.objects.get(id=1)
        field_label = shift._meta.get_field("duration").verbose_name
        self.assertEqual(field_label, "duration")

    def test_shift_type_max_length(self):
        shift = Shift.objects.get(id=1)
        max_length = shift._meta.get_field("shift_type").max_length
        self.assertEqual(max_length, 1)

    def test_str_method(self):
        shift = Shift.objects.get(id=1)
        expected_str = f"{shift.movie.title}, {shift.date}"
        self.assertEqual(str(shift), expected_str)

    def test_user_null(self):
        shift = Shift.objects.get(id=1)
        self.assertIsNone(shift.user)


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("(UserModelTest)")
        # Set up non-modified objects used by all test methods
        get_user_model().objects.create_user(
            username="testbrugernavn",
            email="bamse@kylling.dk",
            password="123asdqwe",
            registered="22-11-2023",
            phone="88888888",
            shifts_taken=69,
        )

    def test_get_by_natural_key(self):
        user = get_user_model().objects.get_by_natural_key(username="testbrugernavn")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testbrugernavn")

    def test_get_absolute_url(self):
        user = get_user_model().objects.get(id=1)
        expected_url = reverse("volunteer-detail", args=[str(user.id)])
        self.assertEqual(user.get_absolute_url(), expected_url)

    def test_username_label(self):
        user = get_user_model().objects.get(id=1)
        field_label = user._meta.get_field("username").verbose_name
        self.assertEqual(field_label, "username")

    def test_registered_label(self):
        user = get_user_model().objects.get(id=1)
        field_label = user._meta.get_field("registered").verbose_name
        self.assertEqual(field_label, "Registration Date")

    def test_phone_label(self):
        user = get_user_model().objects.get(id=1)
        field_label = user._meta.get_field("phone").verbose_name
        self.assertEqual(field_label, "phone")

    def test_shifts_taken_label(self):
        user = get_user_model().objects.get(id=1)
        field_label = user._meta.get_field("shifts_taken").verbose_name
        self.assertEqual(field_label, "Number of shifts taken")

    def test_permissions(self):
        user = get_user_model().objects.get(id=1)
        self.assertFalse(user.has_perm("auth.can_view_users_shifts"))
