from django.contrib import admin

from .models import Film, Comment

# Register your models here.
admin.site.register(Comment)


@admin.register(Film)
class Film(admin.ModelAdmin):

    list_display = ["title", "author", "created_date"]

    list_display_links = ["title", "created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Film
