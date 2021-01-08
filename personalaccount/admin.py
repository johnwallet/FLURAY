from django.contrib import admin

from personalaccount.models import Transaction, RequestChange, CurrencyCBRF

admin.site.register(Transaction)
admin.site.register(RequestChange)
admin.site.register(CurrencyCBRF)

