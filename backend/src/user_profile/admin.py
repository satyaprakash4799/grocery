from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfiles, Addresses, User

# admin.site.register(User, UserAdmin)
admin.site.register(UserProfiles)
admin.site.register(Addresses)
