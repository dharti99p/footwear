from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Register)


@admin.register(Register)
class RegisterUser(admin.ModelAdmin):
    # Specify the fields to display in the list view for the model
    list_display = ['username', 'phone_number', 'email', 'password', 'confirm_password']


# about
@admin.register(About)
class AboutImage(admin.ModelAdmin):
    list_display = ['image']

# header
@admin.register(MenuForm)
class MenuFormEntry(admin.ModelAdmin):
    list_display = ['id', 'title', 'url']


@admin.register(SubMenu)
class SubMenuEntry(admin.ModelAdmin):
    list_display = ['menu_form', 'name', 'url']


@admin.register(BadgeMenu)
class BadgeMenuEntry(admin.ModelAdmin):
    list_display = ['id', 'badge']

# dharti123
