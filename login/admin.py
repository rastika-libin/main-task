from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserRole

class UserRoleAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('role',)}),)

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('role',)}),)

admin.site.register(UserRole, UserRoleAdmin)
admin.site.site_title = "User Administrator - Task"
admin.site.site_header = "User Administration Task"