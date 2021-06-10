from django.contrib import admin

from core.models import Profile, Subscriber


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )

    search_fields = (
        "email",
    )