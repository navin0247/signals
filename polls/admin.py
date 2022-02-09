from django.contrib import admin

from polls.models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list = ['user', 'image']


admin.site.register(Profile, ProfileAdmin)
