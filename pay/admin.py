from django.contrib import admin

from pay.models import Transaction, Currency, TransactionView, Status, SistemChange, RequestChange, TypeChange


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_user', 'transaction_name', 'transaction_status', 'transaction_currency', 'transaction_sum')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Currency, )
admin.site.register(TransactionView, )
admin.site.register(Status, )
admin.site.register(SistemChange, )
admin.site.register(RequestChange, )
admin.site.register(TypeChange, )
