from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    fields = ['title', 'description', 'technology', 'link']

admin.site.register(Project, ProjectAdmin)