from django.contrib import admin

from personalaccount.models import Transaction, Currency, SistemChange, RequestChange, CriteriChange

admin.site.register(CriteriChange)
admin.site.register(Transaction)
admin.site.register(Currency, )
admin.site.register(SistemChange, )
admin.site.register(RequestChange, )
