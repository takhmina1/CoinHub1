from rest_framework import generics
from rest_framework.response import Response
from .models import Cryptocurrency, Portfolio, Order
from .serializers import CryptocurrencySerializer, PortfolioSerializer, OrderSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services import TradingService

class CryptocurrencyListCreateView(generics.ListCreateAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer

    @swagger_auto_schema(
        operation_summary="Получить список криптовалют",
        responses={200: CryptocurrencySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать новую криптовалюту",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Название криптовалюты'),
                'currency_code': openapi.Schema(type=openapi.TYPE_STRING, description='Код валюты'),
                'symbol': openapi.Schema(type=openapi.TYPE_STRING, description='Символ'),
                'country': openapi.Schema(type=openapi.TYPE_STRING, description='Страна')
            }
        ),
        responses={201: CryptocurrencySerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class PortfolioListCreateView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    @swagger_auto_schema(
        operation_summary="Получить список портфелей",
        responses={200: PortfolioSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать новый портфель",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пользователя'),
                'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID криптовалюты'),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Количество')
            }
        ),
        responses={201: PortfolioSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_summary="Получить список ордеров",
        responses={200: OrderSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создать новый ордер",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пользователя'),
                'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID криптовалюты'),
                'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Количество'),
                'order_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['buy', 'sell'], description='Тип ордера (покупка/продажа)')
            }
        ),
        responses={201: OrderSerializer()}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # Добавляем логику для создания ордера и обновления портфеля при создании нового ордера
    def perform_create(self, serializer):
        user = serializer.validated_data['user']
        cryptocurrency = serializer.validated_data['cryptocurrency']
        amount = serializer.validated_data['amount']
        order_type = serializer.validated_data['order_type']

        if order_type == 'buy':
            TradingService.buy_crypto(user, cryptocurrency, amount)
        elif order_type == 'sell':
            TradingService.sell_crypto(user, cryptocurrency, amount)









































































































































































































































































# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Cryptocurrency, Portfolio, Order
# from .serializers import CryptocurrencySerializer, PortfolioSerializer, OrderSerializer
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from .services import *
# from .trading_manager import *

# class CryptocurrencyListCreateView(generics.ListCreateAPIView):
#     queryset = Cryptocurrency.objects.all()
#     serializer_class = CryptocurrencySerializer

#     @swagger_auto_schema(
#         operation_summary="Get list of cryptocurrencies",
#         responses={200: CryptocurrencySerializer(many=True)}
#     )
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)

#     @swagger_auto_schema(
#         operation_summary="Create a new cryptocurrency",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'name': openapi.Schema(type=openapi.TYPE_STRING, description='Cryptocurrency name'),
#                 'currency_code': openapi.Schema(type=openapi.TYPE_STRING, description='Currency code'),
#                 'symbol': openapi.Schema(type=openapi.TYPE_STRING, description='Symbol'),
#                 'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country')
#             }
#         ),
#         responses={201: CryptocurrencySerializer()}
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)

# class PortfolioListCreateView(generics.ListCreateAPIView):
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer

#     @swagger_auto_schema(
#         operation_summary="Get list of portfolios",
#         responses={200: PortfolioSerializer(many=True)}
#     )
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)

#     @swagger_auto_schema(
#         operation_summary="Create a new portfolio",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
#                 'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cryptocurrency ID'),
#                 'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount')
#             }
#         ),
#         responses={201: PortfolioSerializer()}
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)

# class OrderListCreateView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     @swagger_auto_schema(
#         operation_summary="Get list of orders",
#         responses={200: OrderSerializer(many=True)}
#     )
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)

#     @swagger_auto_schema(
#         operation_summary="Create a new order",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
#                 'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cryptocurrency ID'),
#                 'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount'),
#                 'order_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['buy', 'sell'], description='Order type (buy/sell)')
#             }
#         ),
#         responses={201: OrderSerializer()}
#     )
#     def post(self, request, *args, **kwargs):
#         return super().post(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         user = serializer.validated_data['user']
#         cryptocurrency = serializer.validated_data['cryptocurrency']
#         amount = serializer.validated_data['amount']
#         price = serializer.validated_data['price']
#         order_type = serializer.validated_data['order_type']

#         TradingService.place_order(user, cryptocurrency, amount, price, order_type)

#     def perform_update(self, serializer):
#         user = serializer.validated_data['user']
#         cryptocurrency = serializer.validated_data['cryptocurrency']
#         amount = serializer.validated_data['amount']
#         price = serializer.validated_data['price']
#         order_type = serializer.validated_data['order_type']

#         TradingService.place_order(user, cryptocurrency, amount, price, order_type)




























































































































# # from rest_framework import generics
# # from rest_framework.response import Response
# # from .models import Cryptocurrency, Portfolio, Order
# # from .serializers import CryptocurrencySerializer, PortfolioSerializer, OrderSerializer
# # from drf_yasg.utils import swagger_auto_schema
# # from drf_yasg import openapi

# # class CryptocurrencyListCreateView(generics.ListCreateAPIView):
# #     queryset = Cryptocurrency.objects.all()
# #     serializer_class = CryptocurrencySerializer

# #     @swagger_auto_schema(
# #         operation_summary="Get list of cryptocurrencies",
# #         responses={200: CryptocurrencySerializer(many=True)}
# #     )
# #     def get(self, request, *args, **kwargs):
# #         return super().get(request, *args, **kwargs)

# #     @swagger_auto_schema(
# #         operation_summary="Create a new cryptocurrency",
# #         request_body=openapi.Schema(
# #             type=openapi.TYPE_OBJECT,
# #             properties={
# #                 'name': openapi.Schema(type=openapi.TYPE_STRING, description='Cryptocurrency name'),
# #                 'currency_code': openapi.Schema(type=openapi.TYPE_STRING, description='Currency code'),
# #                 'symbol': openapi.Schema(type=openapi.TYPE_STRING, description='Symbol'),
# #                 'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country')
# #             }
# #         ),
# #         responses={201: CryptocurrencySerializer()}
# #     )
# #     def post(self, request, *args, **kwargs):
# #         return super().post(request, *args, **kwargs)

# # class PortfolioListCreateView(generics.ListCreateAPIView):
# #     queryset = Portfolio.objects.all()
# #     serializer_class = PortfolioSerializer

# #     @swagger_auto_schema(
# #         operation_summary="Get list of portfolios",
# #         responses={200: PortfolioSerializer(many=True)}
# #     )
# #     def get(self, request, *args, **kwargs):
# #         return super().get(request, *args, **kwargs)

# #     @swagger_auto_schema(
# #         operation_summary="Create a new portfolio",
# #         request_body=openapi.Schema(
# #             type=openapi.TYPE_OBJECT,
# #             properties={
# #                 'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
# #                 'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cryptocurrency ID'),
# #                 'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount')
# #             }
# #         ),
# #         responses={201: PortfolioSerializer()}
# #     )
# #     def post(self, request, *args, **kwargs):
# #         return super().post(request, *args, **kwargs)

# # class OrderListCreateView(generics.ListCreateAPIView):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer

# #     @swagger_auto_schema(
# #         operation_summary="Get list of orders",
# #         responses={200: OrderSerializer(many=True)}
# #     )
# #     def get(self, request, *args, **kwargs):
# #         return super().get(request, *args, **kwargs)

# #     @swagger_auto_schema(
# #         operation_summary="Create a new order",
# #         request_body=openapi.Schema(
# #             type=openapi.TYPE_OBJECT,
# #             properties={
# #                 'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
# #                 'cryptocurrency': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cryptocurrency ID'),
# #                 'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount'),
# #                 'order_type': openapi.Schema(type=openapi.TYPE_STRING, enum=['buy', 'sell'], description='Order type (buy/sell)')
# #             }
# #         ),
# #         responses={201: OrderSerializer()}
# #     )
# #     def post(self, request, *args, **kwargs):
# #         return super().post(request, *args, **kwargs)
