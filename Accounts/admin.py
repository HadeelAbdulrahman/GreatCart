from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  
from .models import Account, UserProfile        
from django.utils.html import format_html        # Used to safely render HTML in Django admin

#UserAdmin: Used for models that represent a custom user model.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    
    # Fields that will be clickable links in the list view
    list_display_links = ('email', 'first_name', 'last_name')
    
    readonly_fields = ('last_login', 'date_joined') #can't be edited
    ordering = ('-date_joined',)

    # These are used in the built-in UserAdmin but left empty here
    filter_horizontal = ()  # No horizontal filters applied
    list_filter = ()        # No filters in the right sidebar
    fieldsets = ()          # No customized field groupings



#ModelAdmin: Used for regular Django models.
class UserProfileAdmin(admin.ModelAdmin):
    # Method to display the profile picture thumbnail in the admin panel
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url)
        )
    thumbnail.short_description = 'Profile Picture'  # Column title in the admin panel

    # Fields to display in the list view of the admin panel
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

# Register models with custom admin configurations
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
