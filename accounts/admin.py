from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "name",
        "email",
        "username",
        "verified",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", "verified")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "verified")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
