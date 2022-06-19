# social/shout/admin.py

from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, shout

# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "password"]
    inlines = [ProfileInLine]
 

admin.site.unregister(User) # Unregister the user group
admin.site.register(User, UserAdmin) # Register the custom User group that doesn't show the password
admin.site.register(shout) # Registers the shout on the admin site
admin.site.unregister(Group) # Removes the group function in authorization.
# admin.site.register(Profile) # Registers the profile model from the app into the admin site.
