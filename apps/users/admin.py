from django.contrib import admin

from apps.users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff', 'is_active')
