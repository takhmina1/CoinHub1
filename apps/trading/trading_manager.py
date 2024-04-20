from .models import Trade, Order, Portfolio, Cryptocurrency

class TradingManager:
    @staticmethod
    def buy_crypto(user, cryptocurrency, amount, price):
        trade = Trade.objects.create(
            user=user,
            cryptocurrency=cryptocurrency,
            amount=amount,
            price=price,
            trade_type='buy'
        )
        TradingManager._update_portfolio(user, cryptocurrency, amount)

    @staticmethod
    def sell_crypto(user, cryptocurrency, amount, price):
        trade = Trade.objects.create(
            user=user,
            cryptocurrency=cryptocurrency,
            amount=amount,
            price=price,
            trade_type='sell'
        )
        TradingManager._update_portfolio(user, cryptocurrency, -amount)

    @staticmethod
    def place_order(user, cryptocurrency, amount, price, order_type):
        order = Order.objects.create(
            user=user,
            cryptocurrency=cryptocurrency,
            amount=amount,
            price=price,
            order_type=order_type
        )

    @staticmethod
    def user_has_enough_funds(user, amount):
        user_balance = user.balance  # Предположим, что в модели User есть поле balance
        return user_balance >= amount

    @staticmethod
    def user_has_enough_cryptocurrency(user, cryptocurrency, amount):
        portfolio = Portfolio.objects.filter(user=user, cryptocurrency=cryptocurrency).first()
        if portfolio:
            return portfolio.amount >= amount
        else:
            return False















































# from .models import Trade, Order, Portfolio, Cryptocurrency

# class TradingManager:
#     @staticmethod
#     def buy_crypto(user, cryptocurrency, amount, price):
#         trade = Trade.objects.create(
#             user=user,
#             cryptocurrency=cryptocurrency,
#             amount=amount,
#             price=price,
#             trade_type='buy'
#         )
#         TradingManager._update_portfolio(user, cryptocurrency, amount)


#     @staticmethod
#     def sell_crypto(user, cryptocurrency, amount, price):
#         trade = Trade.objects.create(
#             user=user,
#             cryptocurrency=cryptocurrency,
#             amount=amount,
#             price=price,
#             trade_type='sell'
#         )
#         TradingManager._update_portfolio(user, cryptocurrency, -amount)


#     @staticmethod
#     def place_order(user, cryptocurrency, amount, price, order_type):
#         order = Order.objects.create(
#             user=user,
#             cryptocurrency=cryptocurrency,
#             amount=amount,
#             price=price,
#             order_type=order_type
#         )


#     @staticmethod
#     def user_has_enough_funds(user, amount):
#         # Получаем баланс пользователя
#         user_balance = user.balance  # Предположим, что в модели User есть поле balance

#         # Проверяем достаточность средств
#         return user_balance >= amount


#     @staticmethod
#     def user_has_enough_cryptocurrency(user, cryptocurrency, amount):
#         # Получаем портфель пользователя для данной криптовалюты
#         portfolio = Portfolio.objects.filter(user=user, cryptocurrency=cryptocurrency).first()

#         # Проверяем наличие достаточного количества криптовалюты
#         if portfolio:
#             return portfolio.amount >= amount
#         else:
#             return False




























































































# # from .models import *


# # class TradingManager:
# #         @staticmethod
# #         def buy_crypto(user, cryptocurrency, amount, price):
# #             trade = Trade.objects.create(
# #                 user=user,
# #                 cryptocurrency=cryptocurrency,
# #                 amount=amount,
# #                 price=price,
# #                 trade_type='buy'
# #             )
# #             TradingManager._update_portfolio(user, cryptocurrency, amount)


# #         @staticmethod
# #         def sell_crypto(user, cryptocurrency, amount, price):
# #             trade = Trade.objects.create(
# #                 user=user,
# #                 cryptocurrency=cryptocurrency,
# #                 amount=amount,
# #                 price=price,
# #                 trade_type='sell'
# #             )
# #             TradingManager._update_portfolio(user, cryptocurrency, -amount)

# #         # @staticmethod
# #         # def _update_portfolio(user, cryptocurrency, amount):
# #         #     portfolio, created = Portfolio.objects.get_or_create(
# #         #         user=user,
# #         #         cryptocurrency=cryptocurrency
# #         #     )
# #         #     if not created:
# #         #         portfolio.amount += amount
# #         #         portfolio.save()
# #         #     else:
# #         #         Portfolio.objects.create(
# #         #             user=user,
# #         #             cryptocurrency=cryptocurrency,
# #         #             amount=amount
# #         #         )
    

# #         @staticmethod
# #         def place_order(user, cryptocurrency, amount, price, order_type):
# #             order = Order.objects.create(
# #                 user=user,
# #                 cryptocurrency=cryptocurrency,
# #                 amount=amount,
# #                 price=price,
# #                 order_type=order_type
# #             )


# #         @staticmethod
# #         def user_has_enough_funds(user, amount):
# #             # Получаем баланс пользователя
# #             user_balance = user.balance  # Предположим, что в модели User есть поле balance

# #             # Проверяем достаточность средств
# #             return user_balance >= amount

# #         @staticmethod
# #         def user_has_enough_cryptocurrency(user, cryptocurrency, amount):
# #             # Получаем портфель пользователя для данной криптовалюты
# #             portfolio = Portfolio.objects.filter(user=user, cryptocurrency=cryptocurrency).first()

# #             # Проверяем наличие достаточного количества криптовалюты
# #             if portfolio:
# #                 return portfolio.amount >= amount
# #             else:
# #                 return False
