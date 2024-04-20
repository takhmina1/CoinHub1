from decimal import Decimal
from .models import Portfolio, Trade  # Импорт моделей портфеля и сделок
from .trading_manager import TradingManager  # Импорт менеджера торговли

class TradingService:
    # Метод для покупки криптовалюты
    @staticmethod
    def buy_crypto(user, cryptocurrency, amount, price):
        # Проверка на положительное значение количества и цены
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")
        # Проверка достаточности средств на счете пользователя
        if not TradingService.user_has_enough_funds(user, amount * price):
            raise ValueError("Insufficient funds")
        
        # Вызов метода для покупки криптовалюты у менеджера торговли
        TradingManager.buy_crypto(user, cryptocurrency, amount, price)

    # Метод для продажи криптовалюты
    @staticmethod
    def sell_crypto(user, cryptocurrency, amount, price):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")
        if not TradingService.user_has_enough_cryptocurrency(user, cryptocurrency, amount):
            raise ValueError("Insufficient cryptocurrency balance")
        
        TradingManager.sell_crypto(user, cryptocurrency, amount, price)

    # Метод для размещения ордера
    @staticmethod
    def place_order(user, cryptocurrency, amount, price, order_type):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if price <= 0:
            raise ValueError("Price must be positive")

        TradingManager.place_order(user, cryptocurrency, amount, price, order_type)

    # Метод для проверки достаточности средств на счете пользователя
    @staticmethod
    def user_has_enough_funds(user, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return TradingManager.user_has_enough_funds(user, amount)

    # Метод для проверки достаточности криптовалюты у пользователя
    @staticmethod
    def user_has_enough_cryptocurrency(user, cryptocurrency, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return TradingManager.user_has_enough_cryptocurrency(user, cryptocurrency, amount)

    # Метод для получения портфеля пользователя
    @staticmethod
    def get_portfolio(user):
        return Portfolio.objects.filter(user=user)

    # Метод для расчета общей стоимости портфеля пользователя
    @staticmethod
    def calculate_portfolio_value(user):
        portfolio = TradingService.get_portfolio(user)
        total_value = Decimal(0)
        for entry in portfolio:
            total_value += entry.amount * entry.cryptocurrency.exchange_rate
        return total_value

    # Метод для получения последних сделок пользователя
    @staticmethod
    def get_trades(user):
        return Trade.objects.filter(user=user).order_by('-timestamp')[:10]

    # Метод для получения последних ордеров пользователя
    @staticmethod
    def get_orders(user):
        return Order.objects.filter(user=user).order_by('-created_at')[:10]

    # Метод для отмены ордера пользователя
    @staticmethod
    def cancel_order(user, order_id):
        order = Order.objects.get(id=order_id, user=user)
        # Реализация логики отмены ордера
        order.delete()

































































































































































































# from .trading_manager import TradingManager

# class TradingService:
#     @staticmethod
#     def buy_crypto(user, cryptocurrency, amount, price):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         if price <= 0:
#             raise ValueError("Price must be positive")
#         if not TradingService.user_has_enough_funds(user, amount * price):
#             raise ValueError("Insufficient funds")
        
#         TradingManager.buy_crypto(user, cryptocurrency, amount, price)

#     @staticmethod
#     def sell_crypto(user, cryptocurrency, amount, price):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         if price <= 0:
#             raise ValueError("Price must be positive")
#         if not TradingService.user_has_enough_cryptocurrency(user, cryptocurrency, amount):
#             raise ValueError("Insufficient cryptocurrency balance")
        
#         TradingManager.sell_crypto(user, cryptocurrency, amount, price)

#     @staticmethod
#     def place_order(user, cryptocurrency, amount, price, order_type):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         if price <= 0:
#             raise ValueError("Price must be positive")

#         TradingManager.place_order(user, cryptocurrency, amount, price, order_type)

#     @staticmethod
#     def user_has_enough_funds(user, amount):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         return TradingManager.user_has_enough_funds(user, amount)

#     @staticmethod
#     def user_has_enough_cryptocurrency(user, cryptocurrency, amount):
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         return TradingManager.user_has_enough_cryptocurrency(user, cryptocurrency, amount)















































































































# # from .models import Trade, Portfolio
# # from decimal import Decimal

# # class TradingService:
# #     @staticmethod
# #     def buy_crypto(user, cryptocurrency, amount, price):
# #         # Создать новую сделку (Trade) для покупки криптовалюты
# #         trade = Trade.objects.create(
# #             user=user,
# #             cryptocurrency=cryptocurrency,
# #             amount=amount,
# #             price=price,
# #             trade_type='buy'
# #         )
# #         # Обновить портфель пользователя с учетом покупки
# #         TradingService._update_portfolio(user, cryptocurrency, amount)

# #     @staticmethod
# #     def sell_crypto(user, cryptocurrency, amount, price):
# #         # Создать новую сделку (Trade) для продажи криптовалюты
# #         trade = Trade.objects.create(
# #             user=user,
# #             cryptocurrency=cryptocurrency,
# #             amount=amount,
# #             price=price,
# #             trade_type='sell'
# #         )
# #         # Обновить портфель пользователя с учетом продажи
# #         TradingService._update_portfolio(user, cryptocurrency, -amount)

# #     @staticmethod
# #     def _update_portfolio(user, cryptocurrency, amount):
# #         # Попытка получить портфель пользователя для данной криптовалюты
# #         portfolio, created = Portfolio.objects.get_or_create(
# #             user=user,
# #             cryptocurrency=cryptocurrency
# #         )
# #         # Если портфель уже существует, обновляем количество, иначе создаем новый
# #         if not created:
# #             portfolio.amount += amount
# #             portfolio.save()
# #         else:
# #             Portfolio.objects.create(
# #                 user=user,
# #                 cryptocurrency=cryptocurrency,
# #                 amount=amount
# #             )

# #     @staticmethod
# #     def get_portfolio(user):
# #         # Получить портфель пользователя
# #         portfolio = Portfolio.objects.filter(user=user)
# #         return portfolio

# #     @staticmethod
# #     def calculate_portfolio_value(user):
# #         # Рассчитать общую стоимость портфеля пользователя
# #         portfolio = TradingService.get_portfolio(user)
# #         total_value = Decimal(0)
# #         for entry in portfolio:
# #             total_value += entry.amount * entry.cryptocurrency.exchange_rate
# #         return total_value






























































# # # from .models import Cryptocurrency, Portfolio, Order, Trade
# # # from django.db import transaction


# # # class TradingService:
# # #     @staticmethod
# # #     @transaction.atomic
# # #     def buy_crypto(user_id, crypto_symbol, amount, price):
# # #         # Check if the cryptocurrency exists
# # #         cryptocurrency = Cryptocurrency.objects.get(symbol=crypto_symbol)

# # #         # Calculate total cost
# # #         total_cost = amount * price

# # #         # Check if the user has enough funds
# # #         portfolio = Portfolio.objects.get(user_id=user_id, cryptocurrency=cryptocurrency)
# # #         if portfolio.amount < amount:
# # #             raise ValueError("Insufficient funds")

# # #         # Create a buy order
# # #         order = Order.objects.create(user_id=user_id, cryptocurrency=cryptocurrency,
# # #                                      amount=amount, order_type='buy')

# # #         # Create a trade
# # #         trade = Trade.objects.create(user_id=user_id, cryptocurrency=cryptocurrency,
# # #                                      amount=amount, price=price, trade_type='buy')

# # #         # Update portfolio
# # #         portfolio.amount -= amount
# # #         portfolio.save()

# # #         return trade.id

# # #     @staticmethod
# # #     @transaction.atomic
# # #     def sell_crypto(user_id, crypto_symbol, amount, price):
# # #         # Check if the cryptocurrency exists
# # #         cryptocurrency = Cryptocurrency.objects.get(symbol=crypto_symbol)

# # #         # Check if the user has the required amount of cryptocurrency to sell
# # #         portfolio = Portfolio.objects.get(user_id=user_id, cryptocurrency=cryptocurrency)
# # #         if portfolio.amount < amount:
# # #             raise ValueError("Insufficient cryptocurrency balance")

# # #         # Create a sell order
# # #         order = Order.objects.create(user_id=user_id, cryptocurrency=cryptocurrency,
# # #                                      amount=amount, order_type='sell')

# # #         # Create a trade
# # #         trade = Trade.objects.create(user_id=user_id, cryptocurrency=cryptocurrency,
# # #                                      amount=amount, price=price, trade_type='sell')

# # #         # Update portfolio
# # #         portfolio.amount += amount
# # #         portfolio.save()

# # #         return trade.id

# # #     @staticmethod
# # #     def get_portfolio(user_id):
# # #         portfolio = Portfolio.objects.filter(user_id=user_id)
# # #         return portfolio

# # #     @staticmethod
# # #     def get_orders(user_id):
# # #         orders = Order.objects.filter(user_id=user_id)
# # #         return orders

# # #     @staticmethod
# # #     def get_trades(user_id):
# # #         trades = Trade.objects.filter(user_id=user_id)
# # #         return trades
