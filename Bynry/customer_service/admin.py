from django.contrib import admin
from .models import ServiceRequest
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the list display
    list_display = ('username', 'email', 'is_customer', 'is_admin', 'is_staff', 'is_superuser')
    
    # Add your custom fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_customer', 'is_admin')}),
    )

    # Add your custom fields to the add_fieldsets (for creating new users in admin)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_customer', 'is_admin')}),
    )

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('id', 'user', 'service_type', 'status', 'created_at', 'updated_at')

    # Fields that can be edited in the admin detail view
    fields = ('user', 'service_type', 'details', 'attached_file', 'status')

    # Fields that are read-only in the admin detail view
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('service_type', 'details', 'user__username')

