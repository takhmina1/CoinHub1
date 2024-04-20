from django.db import models
from django.utils.translation import gettext_lazy as _

class PaymentSystem(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    api_key = models.CharField(_('API Key'), max_length=200)
    active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.name

class AnalyticalService(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    access_token = models.CharField(_('Access Token'), max_length=200)
    active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.name

class FinancialNewsSource(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    api_key = models.CharField(_('API Key'), max_length=200)
    active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.name

class Integration(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    active = models.BooleanField(_('Active'), default=True)

    payment_systems = models.ManyToManyField(PaymentSystem, verbose_name=_('Payment Systems'), blank=True)
    analytical_services = models.ManyToManyField(AnalyticalService, verbose_name=_('Analytical Services'), blank=True)
    financial_news_sources = models.ManyToManyField(FinancialNewsSource, verbose_name=_('Financial News Sources'), blank=True)

    def __str__(self):
        return self.name

class IntegrationLog(models.Model):
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE, verbose_name=_('Integration'))
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True)
    message = models.TextField(_('Message'))

    class Meta:
        verbose_name_plural = _('Integration Logs')
        ordering = ('-timestamp',)

    def __str__(self):
        return f"{self.integration.name} - {self.timestamp}"

class ExternalService(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    api_key = models.CharField(_('API Key'), max_length=200)
    active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.name

class ExternalServiceUsage(models.Model):
    external_service = models.ForeignKey(ExternalService, on_delete=models.CASCADE, verbose_name=_('External Service'))
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE, verbose_name=_('Integration'))
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True)
    request_data = models.TextField(_('Request Data'))
    response_data = models.TextField(_('Response Data'))

    class Meta:
        verbose_name_plural = _('External Service Usages')
        ordering = ('-timestamp',)

    def __str__(self):
        return f"{self.integration.name} - {self.external_service.name} - {self.timestamp}"

class Notification(models.Model):
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE, verbose_name=_('Integration'))
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True)
    message = models.TextField(_('Message'))

    class Meta:
        verbose_name_plural = _('Notifications')
        ordering = ('-timestamp',)

    def __str__(self):
        return f"{self.integration.name} - {self.timestamp} - {self.message}"

class Task(models.Model):
    integration = models.ForeignKey(Integration, on_delete=models.CASCADE, verbose_name=_('Integration'))
    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    due_date = models.DateField(_('Due Date'))
    completed = models.BooleanField(_('Completed'), default=False)

    class Meta:
        verbose_name_plural = _('Tasks')
        ordering = ('due_date',)

    def __str__(self):
        return self.title
