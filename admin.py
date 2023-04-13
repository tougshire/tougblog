from django.contrib import admin

from tougblog.models import Event, EventDate, Image, Page, Placement, Post

class PlacementAdmin(admin.ModelAdmin):
    list_display = ('title', 'place_number')

admin.site.register(Placement, PlacementAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'draft_status', 'placement', 'list_order')

    def get_queryset(self, request):
        return super().get_queryset(request).model.objects.all()

admin.site.register(Post, PostAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'draft_status')

    prepopulated_fields={'slug': ["title"]}

    def get_queryset(self, request):
        return super().get_queryset(request).model.objects.all()


admin.site.register(Page, PageAdmin)

class EventDateInline(admin.StackedInline):
    model=EventDate
    exta=5

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'draft_status')
    inlines = [EventDateInline,]

    def get_queryset(self, request):
        return super().get_queryset(request).model.objects.all()


admin.site.register(Event, EventAdmin)


admin.site.register(EventDate)

admin.site.register(Image)
