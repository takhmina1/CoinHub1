from django.contrib import admin
from .models import Account, Transaction

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username', 'user__email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'timestamp')
    search_fields = ('account__user__username', 'account__user__email')
    list_filter = ('transaction_type', 'timestamp')























# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('user', 'balance')

# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('account', 'amount', 'transaction_type', 'timestamp')
