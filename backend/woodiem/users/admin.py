from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    search_fields = ["email", "first_name", "last_name"]

    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["pkid", "id", "email"]

    list_filter = ["email", "is_staff", "is_active"]

    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        },
    )


admin.site.register(User, CustomUserAdmin)
