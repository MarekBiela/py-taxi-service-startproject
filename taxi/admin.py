from django.contrib import admin
from .models import Driver, Manufacturer, Car
from django.contrib.auth.admin import UserAdmin


class DriverAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "license_number"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ["license_number"]}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ["license_number"]}),
    )


class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
