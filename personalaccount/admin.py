from django.contrib import admin

from personalaccount.models import Transaction, RequestChange, CurrencyCBRF, StaticDailyProfit, Transfer

admin.site.register(Transaction)
admin.site.register(RequestChange)
admin.site.register(CurrencyCBRF)
admin.site.register(StaticDailyProfit)
admin.site.register(Transfer)

