from django.contrib import admin

from core.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email"
    )

    search_fields = (
        "name",
    )
