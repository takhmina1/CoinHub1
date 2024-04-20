from rest_framework import serializers
from .models import PaymentSystem, AnalyticalService, FinancialNewsSource, Integration, IntegrationLog, ExternalService, ExternalServiceUsage, Notification, Task

class PaymentSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSystem
        fields = '__all__'

class AnalyticalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticalService
        fields = '__all__'

class FinancialNewsSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialNewsSource
        fields = '__all__'

class IntegrationSerializer(serializers.ModelSerializer):
    payment_system_count = serializers.SerializerMethodField()

    class Meta:
        model = Integration
        fields = '__all__'

    def get_payment_system_count(self, obj):
        return obj.payment_systems.count()

class IntegrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationLog
        fields = '__all__'

class ExternalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalService
        fields = '__all__'

class ExternalServiceUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalServiceUsage
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
