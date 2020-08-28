from django.contrib import admin
from .models import SendSms


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    fields = ['fullname', 'date_paid', 'suite_number', 'email', 'phone_no']
    list_display = ('fullname', 'date_paid', 'address', 'suite_number',
                    'phone_no')


admin.site.register(SendSms, AccountAdmin)




