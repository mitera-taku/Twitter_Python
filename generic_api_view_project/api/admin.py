from django.contrib import admin
from .models import MediaPost

@admin.register(MediaPost)
class MediaPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
