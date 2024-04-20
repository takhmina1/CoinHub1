from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cryptocurrency(models.Model):
    # Модель для криптовалюты, хранит информацию о ней
    name = models.CharField(max_length=100)  # Название криптовалюты
    currency_code = models.CharField(max_length=10)  # Код валюты
    symbol = models.CharField(max_length=10)  # Символьный код криптовалюты
    country = models.CharField(max_length=100)  # Страна
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)  # Курс обмена
    market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # Рыночная капитализация

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    # Модель для портфеля пользователя, хранит информацию о криптовалюте в портфеле
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
    amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты в портфеле

    def __str__(self):
        return f'{self.user.username} - {self.cryptocurrency.name}'

class Order(models.Model):
    # Модель для ордера, хранит информацию о совершенных сделках
    ORDER_TYPES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
    amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты
    price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена за единицу криптовалюты
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)  # Тип ордера (Покупка или Продажа)
    created_at = models.DateTimeField(default=timezone.now)  # Время создания ордера

    def __str__(self):
        return f'{self.user.username} - {self.order_type} - {self.amount} {self.cryptocurrency.symbol}'

    def execute_order(self):
        # Метод для выполнения ордера
        if self.order_type == 'buy':
            # Реализация логики для покупки криптовалюты
            # Например, обновление портфеля пользователя с купленной криптовалютой
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            portfolio.amount += self.amount
            portfolio.save()
            # Корректировка баланса пользователя на основе цены ордера
            # Например, вычитание цены из баланса пользователя
            self.user.profile.balance -= self.price
            self.user.profile.save()
        elif self.order_type == 'sell':
            # Реализация логики для продажи криптовалюты
            # Например, обновление портфеля пользователя и баланса соответственно
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            if portfolio.amount >= self.amount:
                portfolio.amount -= self.amount
                portfolio.save()
                # Корректировка баланса пользователя на основе цены ордера
                # Например, добавление цены к балансу пользователя
                self.user.profile.balance += self.price
                self.user.profile.save()
            else:
                raise ValueError("Not enough cryptocurrency in the portfolio to fulfill the sell order")

class Trade(models.Model):
    # Модель для торговой операции, хранит информацию о сделке
    TRADE_TYPES = (
        ('buy', 'Покупка'),
        ('sell', 'Продажа'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
    amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты
    price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена за единицу криптовалюты
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)  # Тип операции (Покупка или Продажа)
    timestamp = models.DateTimeField(auto_now_add=True)  # Время совершения сделки

    def __str__(self):
        return f'{self.user.username} - {self.trade_type} - {self.amount} {self.cryptocurrency.symbol}'

    def save(self, *args, **kwargs):
        self.execute_trade()
        super(Trade, self).save(*args, **kwargs)

    def execute_trade(self):
        # Метод для выполнения сделки
        if self.trade_type == 'buy':
            # Реализация логики для покупки криптовалюты
            # Например, обновление портфеля пользователя с купленной криптовалютой
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            portfolio.amount += self.amount
            portfolio.save()
            # Корректировка баланса пользователя на основе цены сделки
            # Например, вычитание цены из баланса пользователя
            self.user.profile.balance -= self.price
            self.user.profile.save()
        elif self.trade_type == 'sell':
            # Реализация логики для продажи криптовалюты
            # Например, обновление портфеля пользователя и баланса соответственно
            portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
            if portfolio.amount >= self.amount:
                portfolio.amount -= self.amount
                portfolio.save()
                # Корректировка баланса пользователя на основе цены сделки
                # Например, добавление цены к балансу пользователя
                self.user.profile.balance += self.price
                self.user.profile.save()
            else:
                # Обработка случая недостаточного количества криптовалюты в портфеле
                 raise ValueError("Not enough cryptocurrency in the portfolio to fulfill the sell order")


            



















































































































































































































# # # from django.db import models
# # # from django.contrib.auth.models import User

# # # from django.utils import timezone


# # # class Cryptocurrency(models.Model):
# # #     name = models.CharField(max_length=100)
# # #     currency_code = models.CharField(max_length=10)
# # #     symbol = models.CharField(max_length=10)
# # #     country = models.CharField(max_length=100)
# # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)



# # # class Portfolio(models.Model):
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
    



# # # class Order(models.Model):
# # #     ORDER_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
# # #     created_at = models.DateTimeField(default=timezone.now)





# # # class Trade(models.Model):
# # #     TRADE_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # #     timestamp = models.DateTimeField(auto_now_add=True)

    
































































































































































# # # from django.db import models
# # # from django.contrib.auth.models import User

# # # class Cryptocurrency(models.Model):
# # #     name = models.CharField(max_length=100)
# # #     currency_code = models.CharField(max_length=10)
# # #     symbol = models.CharField(max_length=10)
# # #     country = models.CharField(max_length=100)
# # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

# # # class Portfolio(models.Model):
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # class Order(models.Model):
# # #     ORDER_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)

# # # class Trade(models.Model):
# # #     TRADE_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # #     timestamp = models.DateTimeField(auto_now_add=True)

# # # # Вспомогательные функции для управления торговлей
# # # class TradingManager:
# # #     @staticmethod
# # #     def buy_crypto(user, cryptocurrency, amount, price):
# # #         # Создать новую сделку (Trade) для покупки криптовалeshe chot mojno dovait dly etoy realnomu projectu dly etoy logikoyюты
# # #         trade = Trade.objects.create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency,
# # #             amount=amount,
# # #             price=price,
# # #             trade_type='buy'
# # #         )
# # #         # Обновить портфель пользователя с учетом покупки
# # #         TradingManager._update_portfolio(user, cryptocurrency, amount)

# # #     @staticmethod
# # #     def sell_crypto(user, cryptocurrency, amount, price):
# # #         # Создать новую сделку (Trade) для продажи криптовалюты
# # #         trade = Trade.objects.create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency,
# # #             amount=amount,
# # #             price=price,
# # #             trade_type='sell'
# # #         )
# # #         # Обновить портфель пользователя с учетом продажи
# # #         TradingManager._update_portfolio(user, cryptocurrency, -amount)

# # #     @staticmethod
# # #     def _update_portfolio(user, cryptocurrency, amount):
# # #         # Попытка получить портфель пользователя для данной криптовалюты
# # #         portfolio, created = Portfolio.objects.get_or_create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency
# # #         )
# # #         # Если портфель уже существует, обновляем количество, иначе создаем новый
# # #         if not created:
# # #             portfolio.amount += amount
# # #             portfolio.save()
# # #         else:
# # #             Portfolio.objects.create(
# # #                 user=user,
# # #                 cryptocurrency=cryptocurrency,
# # #                 amount=amount
# # #             )




























































































































































# # # # from django.db import models
# # # # from django.contrib.auth.models import User

# # # # class Cryptocurrency(models.Model):
# # # #     name = models.CharField(max_length=100)
# # # #     currency_code = models.CharField(max_length=10)
# # # #     symbol = models.CharField(max_length=10)
# # # #     country = models.CharField(max_length=100)
# # # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
   

# # # # class Portfolio(models.Model):
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # # class Order(models.Model):
# # # #     ORDER_TYPES = (
# # # #         ('buy', 'Buy'),
# # # #         ('sell', 'Sell'),
# # # #     )
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)

# # # # class Trade(models.Model):
# # # #     TRADE_TYPES = (
# # # #         ('buy', 'Buy'),
# # # #         ('sell', 'Sell'),
# # # #     )
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # # #     timestamp = models.DateTimeField(auto_now_add=True)


















































# # # # # from django.db import models
# # # # # from django.contrib.auth.models import User

# # # # # class Cryptocurrency(models.Model):
# # # # #     name = models.CharField(max_length=100)
# # # # #     currency_code = models.CharField(max_length=10)
# # # # #     symbol = models.CharField(max_length=10)
# # # # #     country = models.CharField(max_length=100)
# # # # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # # # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
# # # # #     # Другие поля могут быть добавлены по необходимости

# # # # # class Portfolio(models.Model):
# # # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # # # class Order(models.Model):
# # # # #     ORDER_TYPES = (
# # # # #         ('buy', 'Buy'),
# # # # #         ('sell', 'Sell'),
# # # # #     )
# # # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)




























































































































































# # # # # # from django.db import models


# # # # # # class Trading:
# # # # # #     def __init__(self):
# # # # # #         pass
    
# # # # # #     def buy_crypto(self, user_id, crypto_symbol, amount, price):
        
        
# # # # # #         transaction_details = {
# # # # # #             'user_id': user_id,
# # # # # #             'crypto_symbol': crypto_symbol,
# # # # # #             'amout': amout,
# # # # # #             'price': price,
# # # # # #             'type': 'buy'
# # # # # #         }
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
#     from django.db import models
# # from django.contrib.auth.models import User
# # from django.utils import timezone

# # class Cryptocurrency(models.Model):
# #     # Модель для криптовалюты, хранит информацию о ней
# #     name = models.CharField(max_length=100)  # Название криптовалюты
# #     currency_code = models.CharField(max_length=10)  # Код валюты
# #     symbol = models.CharField(max_length=10)  # Символьный код криптовалюты
# #     country = models.CharField(max_length=100)  # Страна
# #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)  # Курс обмена
# #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)  # Рыночная капитализация

# #     def __str__(self):
# #         return self.name

# # class Portfolio(models.Model):
# #     # Модель для портфеля пользователя, хранит информацию о криптовалюте в портфеле
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
# #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
# #     amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты в портфеле

# #     def __str__(self):
# #         return f'{self.user.username} - {self.cryptocurrency.name}'

# # class Order(models.Model):
# #     # Модель для ордера, хранит информацию о совершенных сделках
# #     ORDER_TYPES = (
# #         ('buy', 'Покупка'),
# #         ('sell', 'Продажа'),
# #     )
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
# #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
# #     amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты
# #     price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена за единицу криптовалюты
# #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)  # Тип ордера (Покупка или Продажа)
# #     created_at = models.DateTimeField(default=timezone.now)  # Время создания ордера

# #     def __str__(self):
# #         return f'{self.user.username} - {self.order_type} - {self.amount} {self.cryptocurrency.symbol}'

# #     def execute_order(self):
# #         # Метод для выполнения ордера
# #         if self.order_type == 'buy':
# #             # Реализация логики для покупки криптовалюты
# #             # Например, обновление портфеля пользователя с купленной криптовалютой
# #             portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
# #             portfolio.amount += self.amount
# #             portfolio.save()
# #             # Корректировка баланса пользователя на основе цены ордера
# #             # Например, вычитание цены из баланса пользователя
# #             self.user.profile.balance -= self.price
# #             self.user.profile.save()
# #         elif self.order_type == 'sell':
# #             # Реализация логики для продажи криптовалюты
# #             # Например, обновление портфеля пользователя и баланса соответственно
# #             portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
# #             if portfolio.amount >= self.amount:
# #                 portfolio.amount -= self.amount
# #                 portfolio.save()
# #                 # Корректировка баланса пользователя на основе цены ордера
# #                 # Например, добавление цены к балансу пользователя
# #                 self.user.profile.balance += self.price
# #                 self.user.profile.save()
# #             else:
# #                 # Обработка случая недостаточного количества криптовалюты в портфеле
# #                 pass

# # class Trade(models.Model):
# #     # Модель для торговой операции, хранит информацию о сделке
# #     TRADE_TYPES = (
# #         ('buy', 'Покупка'),
# #         ('sell', 'Продажа'),
# #     )
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
# #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)  # Криптовалюта
# #     amount = models.DecimalField(max_digits=20, decimal_places=10)  # Количество криптовалюты
# #     price = models.DecimalField(max_digits=20, decimal_places=10)  # Цена за единицу криптовалюты
# #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)  # Тип операции (Покупка или Продажа)
# #     timestamp = models.DateTimeField(auto_now_add=True)  # Время совершения сделки

# #     def __str__(self):
# #         return f'{self.user.username} - {self.trade_type} - {self.amount} {self.cryptocurrency.symbol}'

# #     def save(self, *args, **kwargs):
# #         self.execute_trade()
# #         super(Trade, self).save(*args, **kwargs)

# #     def execute_trade(self):
# #         # Метод для выполнения сделки
# #         if self.trade_type == 'buy':
# #             # Реализация логики для покупки криптовалюты
# #             # Например, обновление портфеля пользователя с купленной криптовалютой
# #             portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
# #             portfolio.amount += self.amount
# #             portfolio.save()
# #             # Корректировка баланса пользователя на основе цены сделки
# #             # Например, вычитание цены из баланса пользователя
# #             self.user.profile.balance -= self.price
# #             self.user.profile.save()
# #         elif self.trade_type == 'sell':
# #             # Реализация логики для продажи криптовалюты
# #             # Например, обновление портфеля пользователя и баланса соответственно
# #             portfolio, created = Portfolio.objects.get_or_create(user=self.user, cryptocurrency=self.cryptocurrency)
# #             if portfolio.amount >= self.amount:
# #                 portfolio.amount -= self.amount
# #                 portfolio.save()
# #                 # Корректировка баланса пользователя на основе цены сделки
# #                 # Например, добавление цены к балансу пользователя
# #                 self.user.profile.balance += self.price
# #                 self.user.profile.save()
# #             else:
# #                 # Обработка случая недостаточного количества криптовалюты в портфеле
# #                 pass
            



















































































































































































































# # # from django.db import models
# # # from django.contrib.auth.models import User

# # # from django.utils import timezone


# # # class Cryptocurrency(models.Model):
# # #     name = models.CharField(max_length=100)
# # #     currency_code = models.CharField(max_length=10)
# # #     symbol = models.CharField(max_length=10)
# # #     country = models.CharField(max_length=100)
# # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)



# # # class Portfolio(models.Model):
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
    



# # # class Order(models.Model):
# # #     ORDER_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
# # #     created_at = models.DateTimeField(default=timezone.now)





# # # class Trade(models.Model):
# # #     TRADE_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # #     timestamp = models.DateTimeField(auto_now_add=True)

    
































































































































































# # # from django.db import models
# # # from django.contrib.auth.models import User

# # # class Cryptocurrency(models.Model):
# # #     name = models.CharField(max_length=100)
# # #     currency_code = models.CharField(max_length=10)
# # #     symbol = models.CharField(max_length=10)
# # #     country = models.CharField(max_length=100)
# # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

# # # class Portfolio(models.Model):
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # class Order(models.Model):
# # #     ORDER_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)

# # # class Trade(models.Model):
# # #     TRADE_TYPES = (
# # #         ('buy', 'Buy'),
# # #         ('sell', 'Sell'),
# # #     )
# # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # #     timestamp = models.DateTimeField(auto_now_add=True)

# # # # Вспомогательные функции для управления торговлей
# # # class TradingManager:
# # #     @staticmethod
# # #     def buy_crypto(user, cryptocurrency, amount, price):
# # #         # Создать новую сделку (Trade) для покупки криптовалeshe chot mojno dovait dly etoy realnomu projectu dly etoy logikoyюты
# # #         trade = Trade.objects.create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency,
# # #             amount=amount,
# # #             price=price,
# # #             trade_type='buy'
# # #         )
# # #         # Обновить портфель пользователя с учетом покупки
# # #         TradingManager._update_portfolio(user, cryptocurrency, amount)

# # #     @staticmethod
# # #     def sell_crypto(user, cryptocurrency, amount, price):
# # #         # Создать новую сделку (Trade) для продажи криптовалюты
# # #         trade = Trade.objects.create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency,
# # #             amount=amount,
# # #             price=price,
# # #             trade_type='sell'
# # #         )
# # #         # Обновить портфель пользователя с учетом продажи
# # #         TradingManager._update_portfolio(user, cryptocurrency, -amount)

# # #     @staticmethod
# # #     def _update_portfolio(user, cryptocurrency, amount):
# # #         # Попытка получить портфель пользователя для данной криптовалюты
# # #         portfolio, created = Portfolio.objects.get_or_create(
# # #             user=user,
# # #             cryptocurrency=cryptocurrency
# # #         )
# # #         # Если портфель уже существует, обновляем количество, иначе создаем новый
# # #         if not created:
# # #             portfolio.amount += amount
# # #             portfolio.save()
# # #         else:
# # #             Portfolio.objects.create(
# # #                 user=user,
# # #                 cryptocurrency=cryptocurrency,
# # #                 amount=amount
# # #             )




























































































































































# # # # from django.db import models
# # # # from django.contrib.auth.models import User

# # # # class Cryptocurrency(models.Model):
# # # #     name = models.CharField(max_length=100)
# # # #     currency_code = models.CharField(max_length=10)
# # # #     symbol = models.CharField(max_length=10)
# # # #     country = models.CharField(max_length=100)
# # # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
   

# # # # class Portfolio(models.Model):
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # # class Order(models.Model):
# # # #     ORDER_TYPES = (
# # # #         ('buy', 'Buy'),
# # # #         ('sell', 'Sell'),
# # # #     )
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)

# # # # class Trade(models.Model):
# # # #     TRADE_TYPES = (
# # # #         ('buy', 'Buy'),
# # # #         ('sell', 'Sell'),
# # # #     )
# # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     price = models.DecimalField(max_digits=20, decimal_places=10)
# # # #     trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
# # # #     timestamp = models.DateTimeField(auto_now_add=True)


















































# # # # # from django.db import models
# # # # # from django.contrib.auth.models import User

# # # # # class Cryptocurrency(models.Model):
# # # # #     name = models.CharField(max_length=100)
# # # # #     currency_code = models.CharField(max_length=10)
# # # # #     symbol = models.CharField(max_length=10)
# # # # #     country = models.CharField(max_length=100)
# # # # #     exchange_rate = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
# # # # #     market_capitalization = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
# # # # #     # Другие поля могут быть добавлены по необходимости

# # # # # class Portfolio(models.Model):
# # # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# # # # # class Order(models.Model):
# # # # #     ORDER_TYPES = (
# # # # #         ('buy', 'Buy'),
# # # # #         ('sell', 'Sell'),
# # # # #     )
# # # # #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # # # #     cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
# # # # #     amount = models.DecimalField(max_digits=20, decimal_places=10)
# # # # #     order_type = models.CharField(max_length=4, choices=ORDER_TYPES)




























































































































































# # # # # # from django.db import models


# # # # # # class Trading:
# # # # # #     def __init__(self):
# # # # # #         pass
    
# # # # # #     def buy_crypto(self, user_id, crypto_symbol, amount, price):
        
        
# # # # # #         transaction_details = {
# # # # # #             'user_id': user_id,
# # # # # #             'crypto_symbol': crypto_symbol,
# # # # # #             'amout': amout,
# # # # # #             'price': price,
# # # # # #             'type': 'buy'
# # # # # #         }
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
