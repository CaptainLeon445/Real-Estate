from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=["id", "uu_id", "user", "gender", "phonenumber", "country", "city"]
    list_filter=["gender", "country", "city"]
    list_display_links=["id", "uu_id", "user"]

admin.site.register(Profile, ProfileAdmin)