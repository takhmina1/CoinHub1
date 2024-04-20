from django.contrib import admin
from .models import Cryptocurrency, Portfolio, Order, Trade

class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'currency_code', 'symbol', 'country', 'exchange_rate', 'market_capitalization')

admin.site.register(Cryptocurrency, CryptocurrencyAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency', 'amount')

admin.site.register(Portfolio, PortfolioAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency', 'amount', 'price', 'order_type', 'created_at')

    def execute_order(self, request, queryset):
        for order in queryset:
            order.execute_order()

    execute_order.short_description = "Execute selected orders"

    actions = [execute_order]

admin.site.register(Order, OrderAdmin)

class TradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'cryptocurrency', 'amount', 'price', 'trade_type', 'timestamp')

    def execute_trade(self, request, queryset):
        for trade in queryset:
            trade.execute_trade()

    execute_trade.short_description = "Execute selected trades"

    actions = [execute_trade]

admin.site.register(Trade, TradeAdmin)





































# from django.contrib import admin
# from .models import Cryptocurrency, Portfolio, Order, Trade

# @admin.register(Cryptocurrency)
# class CryptocurrencyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'currency_code', 'symbol', 'country', 'exchange_rate', 'market_capitalization')
#     search_fields = ('name', 'currency_code', 'symbol')

# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('user', 'cryptocurrency', 'amount')
#     search_fields = ('user__username', 'cryptocurrency__name')

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user', 'cryptocurrency', 'amount', 'order_type')
#     list_filter = ('order_type',)
#     search_fields = ('user__username', 'cryptocurrency__name')

# @admin.register(Trade)
# class TradeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'cryptocurrency', 'amount', 'price', 'trade_type', 'timestamp')
#     list_filter = ('trade_type',)
#     search_fields = ('user__username', 'cryptocurrency__name')
#     date_hierarchy = 'timestamp'

































# # from django.contrib import admin
# # from .models import Cryptocurrency, Portfolio, Order, Trade

# # @admin.register(Cryptocurrency)
# # class CryptocurrencyAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'currency_code', 'symbol', 'country', 'exchange_rate', 'market_capitalization')
# #     search_fields = ('name', 'currency_code', 'symbol')

# # @admin.register(Portfolio)
# # class PortfolioAdmin(admin.ModelAdmin):
# #     list_display = ('user', 'cryptocurrency', 'amount')
# #     search_fields = ('user__username', 'cryptocurrency__name')

# # @admin.register(Order)
# # class OrderAdmin(admin.ModelAdmin):
# #     list_display = ('user', 'cryptocurrency', 'amount', 'order_type')
# #     list_filter = ('order_type',)
# #     search_fields = ('user__username', 'cryptocurrency__name')

# # @admin.register(Trade)
# # class TradeAdmin(admin.ModelAdmin):
# #     list_display = ('user', 'cryptocurrency', 'amount', 'price', 'trade_type', 'timestamp')
# #     list_filter = ('trade_type',)
# #     search_fields = ('user__username', 'cryptocurrency__name')
# #     date_hierarchy = 'timestamp'
