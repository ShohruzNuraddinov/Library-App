from django.contrib import admin

from apps.library import models
# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "genre")
    search_fields = ("title", "author__name")
    list_filter = ("published_date",)
    ordering = ("-published_date",)


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date", "death_date")
    search_fields = ("full_name",)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "rate")
    search_fields = ("book__title", "user__email")
    ordering = ("-created_at",)
