from django.contrib import admin
from .models import PaymentSystem, AnalyticalService, FinancialNewsSource, Integration, IntegrationLog, ExternalService, ExternalServiceUsage, Notification, Task

@admin.register(PaymentSystem)
class PaymentSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_key', 'active')
    search_fields = ('name', 'api_key')
    list_filter = ('active',)

    def toggle_active(self, request, queryset):
        for payment_system in queryset:
            payment_system.active = not payment_system.active
            payment_system.save()
            

    toggle_active.short_description = 'Toggle Active'
    actions = [toggle_active]

@admin.register(AnalyticalService)
class AnalyticalServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'access_token', 'active')
    search_fields = ('name', 'access_token')
    list_filter = ('active',)

    def toggle_active(self, request, queryset):
        for analytical_service in queryset:
            analytical_service.active = not analytical_service.active
            analytical_service.save()
            

    toggle_active.short_description = 'Toggle Active'
    actions = [toggle_active]

@admin.register(FinancialNewsSource)
class FinancialNewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_key', 'active')
    search_fields = ('name', 'api_key')
    list_filter = ('active',)

    def toggle_active(self, request, queryset):
        for financial_news_source in queryset:
            financial_news_source.active = not financial_news_source.active
            financial_news_source.save()
           

    toggle_active.short_description = 'Toggle Active'
    actions = [toggle_active]






























































# from django.contrib import admin
# from .models import PaymentSystem, AnalyticalService, FinancialNewsSource, Integration, IntegrationLog, ExternalService, ExternalServiceUsage, Notification, Task

# @admin.register(PaymentSystem)
# class PaymentSystemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'api_key', 'active')
#     search_fields = ('name', 'api_key')
#     list_filter = ('active',)

#     def toggle_active(self, request, queryset):
#         queryset.update(active=not queryset.first().active)

#     toggle_active.short_description = 'Toggle Active'
#     actions = [toggle_active]

# @admin.register(AnalyticalService)
# class AnalyticalServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'access_token', 'active')
#     search_fields = ('name', 'access_token')
#     list_filter = ('active',)

#     def toggle_active(self, request, queryset):
#         queryset.update(active=not queryset.first().active)

#     toggle_active.short_description = 'Toggle Active'
#     actions = [toggle_active]

# @admin.register(FinancialNewsSource)
# class FinancialNewsSourceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'api_key', 'active')
#     search_fields = ('name', 'api_key')
#     list_filter = ('active',)

#     def toggle_active(self, request, queryset):
#         queryset.update(active=not queryset.first().active)

#     toggle_active.short_description = 'Toggle Active'
#     actions = [toggle_active]

# @admin.register(Integration)
# class IntegrationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'active')
#     search_fields = ('name', 'description')
#     list_filter = ('active',)

#     def toggle_active(self, request, queryset):
#         queryset.update(active=not queryset.first().active)

#     toggle_active.short_description = 'Toggle Active'
#     actions = [toggle_active]

# @admin.register(IntegrationLog)
# class IntegrationLogAdmin(admin.ModelAdmin):
#     list_display = ('integration', 'timestamp', 'message')
#     search_fields = ('integration__name', 'message')
#     list_filter = ('timestamp',)

# @admin.register(ExternalService)
# class ExternalServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'api_key', 'active')
#     search_fields = ('name', 'description', 'api_key')
#     list_filter = ('active',)

#     def toggle_active(self, request, queryset):
#         queryset.update(active=not queryset.first().active)

#     toggle_active.short_description = 'Toggle Active'
#     actions = [toggle_active]

# @admin.register(ExternalServiceUsage)
# class ExternalServiceUsageAdmin(admin.ModelAdmin):
#     list_display = ('external_service', 'integration', 'timestamp', 'request_data', 'response_data')
#     search_fields = ('external_service__name', 'integration__name', 'request_data', 'response_data')
#     list_filter = ('timestamp',)

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('integration', 'timestamp', 'message')
#     search_fields = ('integration__name', 'message')
#     list_filter = ('timestamp',)

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('integration', 'title', 'description', 'due_date', 'completed')
#     search_fields = ('integration__name', 'title', 'description')
#     list_filter = ('due_date', 'completed')
