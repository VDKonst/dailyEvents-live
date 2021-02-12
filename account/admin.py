from django.contrib import admin
from .models import Account, City, OrgApplication, OwnerApplication
from django.contrib.auth.admin import UserAdmin


class CityAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('slug', )

admin.site.register(Account)

admin.site.register(City,CityAdmin)

admin.site.register(OwnerApplication)

admin.site.register(OrgApplication)
