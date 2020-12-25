from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# view site url
admin.site.site_url = "/"

# timeformat
from django.conf.locale.en import formats as en_formats

en_formats.DATETIME_FORMAT = "Y. m. d, H:i"



class AccountAdmin(UserAdmin):
    list_display = ("email", "last_name", "first_name", "date_joined", "last_login", "is_admin", "is_staff", "is_active")
    search_fields = ("email", "last_name", "first_name")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("email",)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)