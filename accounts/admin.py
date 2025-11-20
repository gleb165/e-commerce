from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address


class AddressInline(admin.StackedInline):
    model = Address
    fields = (
        'city',
        'region',
        'street',
        'building',
        'apartment',
        'delivery_type',
        'post_office_ref',
        'post_office_address',
    )
    extra = 0


class CustomUserAdmin(UserAdmin):
    model = User
    inlines = [AddressInline]

    list_display = ['email', 'username', 'phone_number', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username', 'phone_number']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email','phone_number', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )


admin.site.register(Address)
admin.site.register(User, CustomUserAdmin)
