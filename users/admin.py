from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_of_birth', 'is_admin']
    list_filter = ['is_admin']
    list_editable = ['is_admin']