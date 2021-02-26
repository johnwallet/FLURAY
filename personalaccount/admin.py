from django.contrib import admin

from personalaccount.models import Transaction, RequestChange, CurrencyCBRF, StaticDailyProfit, Transfer, News, \
    PSFormNow

admin.site.register(Transaction)
admin.site.register(RequestChange)
admin.site.register(CurrencyCBRF)
admin.site.register(StaticDailyProfit)
admin.site.register(Transfer)
admin.site.register(News)
admin.site.register(PSFormNow)
