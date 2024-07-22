from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import UserCreateForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = (
        'phone', 'first_name', 'last_name', 'is_superuser', 'is_verified', 'is_active', 'created_date',)
    list_filter = ('email', 'is_active')
    fieldsets = (
        ('Information', {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_active', 'is_verified', 'is_superuser',)}),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password1', 'password2', 'is_active', 'is_verified', 'is_superuser',)
            }),
    )
    search_fields = ('email', 'phone',)
    ordering = ('-created_date',)
    readonly_fields = ('password',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'expiration_date',)
