from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("email", "name", "is_staff", "is_active")
    ordering = ("id",)
    search_fields = ("email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "password",
                    "role",
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2", "role"),
            },
        ),
    )
