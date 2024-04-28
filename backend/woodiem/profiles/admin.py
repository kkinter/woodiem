from django.contrib import admin

from .forms import ProfileForm
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
    ]
    list_display_links = ["pkid", "id", "user"]
    list_filter = ["id", "pkid"]
    form = ProfileForm


admin.site.register(Profile, ProfileAdmin)
