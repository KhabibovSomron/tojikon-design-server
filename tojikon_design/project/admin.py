from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Project, Image, Category, Video 

# Register your models here.

admin.site.site_header = "Tojikon Design Administration"
admin.site.unregister(Group)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'link')

