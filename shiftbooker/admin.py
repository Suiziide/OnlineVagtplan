from django.contrib import admin
from .models import Shift, Movie

# Define the admin classes
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'duration', 'poster')
    list_filter = ('title', 'date', 'duration')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_type', 'duration','movie', 'user', 'date')
    list_filter = ('shift_type', 'date', 'duration', 'movie', 'user', 'date')