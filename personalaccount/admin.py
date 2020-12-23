from django.contrib import admin

from personalaccount.models import Transaction, RequestChange

admin.site.register(Transaction)
admin.site.register(RequestChange, )
