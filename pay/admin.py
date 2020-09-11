from django.contrib import admin

from pay.models import Transaction, Currency, SistemChange, RequestChange


admin.site.register(Transaction)
admin.site.register(Currency, )
admin.site.register(SistemChange, )
admin.site.register(RequestChange, )
