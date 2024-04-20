from rest_framework import serializers
from .models import Cryptocurrency, Portfolio, Order, Trade


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'
        
        

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
        
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.execute_order()
        return order

    def update(self, instance, validated_data):
        # Implement logic for updating order (if needed)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.price = validated_data.get('price', instance.price)
        instance.order_type = validated_data.get('order_type', instance.order_type)
        instance.save()
        return instance
    
    
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

    def create(self, validated_data):
        trade = Trade.objects.create(**validated_data)
        trade.execute_trade()
        return trade

    def update(self, instance, validated_data):
        # Получаем текущий статус сделки
        current_status = instance.status

        # Проверяем, можно ли обновить сделку в текущем статусе
        if current_status == 'open':
            # Пример: Обновляем количество и цену сделки
            instance.amount = validated_data.get('amount', instance.amount)
            instance.price = validated_data.get('price', instance.price)
            instance.save()
            return instance
        else:
            # Если статус сделки не позволяет обновление, возбуждаем исключение
            raise serializers.ValidationError("Нельзя обновить сделку в текущем статусе")






















































# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Cryptocurrency, Portfolio, Order, Trade

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email']

# class CryptocurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cryptocurrency
#         fields = '__all__'

# class PortfolioSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     cryptocurrency = CryptocurrencySerializer()

#     class Meta:
#         model = Portfolio
#         fields = ['user', 'cryptocurrency', 'amount']

# class OrderSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     cryptocurrency = CryptocurrencySerializer()

#     class Meta:
#         model = Order
#         fields = '__all__'


# class TradeSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     cryptocurrency = CryptocurrencySerializer()

#     class Meta:
#         model = Trade
#         fields = ['user', 'cryptocurrency', 'amount', 'price', 'trade_type', 'timestamp']




















































# # from rest_framework import serializers
# # from .models import Cryptocurrency, Portfolio, Order, Trade
# # from django.contrib.auth.models import User

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = ['id', 'username', 'email']

# # class CryptocurrencySerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Cryptocurrency
# #         fields = '__all__'

# # class PortfolioSerializer(serializers.ModelSerializer):
# #     user = UserSerializer()
# #     cryptocurrency = CryptocurrencySerializer()

# #     class Meta:
# #         model = Portfolio
# #         fields = ['user', 'cryptocurrency', 'amount']

# # class OrderSerializer(serializers.ModelSerializer):
# #     user = UserSerializer()
# #     cryptocurrency = CryptocurrencySerializer()

# #     class Meta:
# #         model = Order
# #         fields = ['user', 'cryptocurrency', 'amount', 'order_type']

# # class TradeSerializer(serializers.ModelSerializer):
# #     user = UserSerializer()
# #     cryptocurrency = CryptocurrencySerializer()

# #     class Meta:
# #         model = Trade
# #         fields = ['user', 'cryptocurrency', 'amount', 'price', 'trade_type', 'timestamp']
