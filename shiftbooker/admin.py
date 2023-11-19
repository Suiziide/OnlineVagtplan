from django.contrib import admin
from .models import Shift, Movie
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

# Register your models here.

class UserAdmin(BaseUserAdmin):
  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('username', 'email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'shifts_taken')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('username', 'phone', 'password1', 'password2'),
      }),
  )
  list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', "phone"]
  search_fields = ('username', 'email', 'first_name', 'last_name')
  ordering = ('username', )

admin.site.register(User, UserAdmin)

# Define the admin classes
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "duration", "poster")
    list_filter = ("title", "date", "duration")


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("shift_type", "duration", "movie", "user", "date")
    list_filter = ("shift_type", "date", "duration", "movie", "user", "date")
