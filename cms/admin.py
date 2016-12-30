from django.contrib import admin
from cms.models import User, Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'distance', 'date',)
    list_display_links = ('id', 'user', 'distance', 'date',)
admin.site.register(Track, TrackAdmin)