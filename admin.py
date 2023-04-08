from django.contrib import admin

from sdchomepage.models import Event, EventDate, Image, Placement, Post

class PlacementAdmin(admin.ModelAdmin):
    list_display = ('title', 'list_order')

admin.site.register(Placement, PlacementAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'placement', 'list_order')

admin.site.register(Post, PostAdmin)

class EventDateInline(admin.StackedInline):
    model=EventDate
    exta=5

class EventAdmin(admin.ModelAdmin):
    inlines = [EventDateInline,]

admin.site.register(Event, EventAdmin)


admin.site.register(EventDate)

admin.site.register(Image)