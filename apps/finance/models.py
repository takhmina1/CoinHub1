from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class Currency(models.Model):
    """Валюта"""

    symbol = models.CharField(verbose_name='Символ валюты', max_length=2)
    code = models.CharField(
        verbose_name='Код валюты',
        validators=[MinValueValidator(3)],
        max_length=3,
        unique=True,
    )
    short_name = models.CharField(verbose_name='Краткое название', max_length=3)
    full_name = models.CharField(verbose_name='Полное название', max_length=50)

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.full_name


class Account(models.Model):
    """Счет"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account')
    currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Account of {self.user.username}"

    def deposit(self, amount):
        """Пополнение баланса"""
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        """Вывод средств"""
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False


class Transaction(models.Model):
    """Транзакция"""

    TRANSACTION_TYPES = (
        ('deposit', 'Пополнение'),
        ('withdrawal', 'Вывод средств'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} for account {self.account}"



class Application(models.Model):
    """Заявка на ввод/вывод средств"""

    account = models.ForeignKey(Account, verbose_name='Счет', on_delete=models.SET_NULL, null=True)
    currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.SET_NULL, null=True)

    payment_id = models.UUIDField(verbose_name="Id платежа", unique=True, editable=False, blank=True, null=True)
    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=11,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
    type = models.CharField(verbose_name='Тип платежа', choices=Transaction.TRANSACTION_TYPES, max_length=20)
    status = models.CharField(verbose_name='Статус', max_length=20)

    def __str__(self):
        return f"{self.get_type_display()} application of {self.amount} for account {self.account}"



class ApplicationLog(models.Model):
    """История изменений заявки"""

    application = models.ForeignKey(Application, verbose_name='Заявка', on_delete=models.SET_NULL, null=True)

    status = models.CharField(verbose_name='Статус', max_length=20)

    def __str__(self):
        return f"Log for {self.application}: {self.status}"



class Customer(models.Model):
    """Клиент"""

    name = models.CharField(verbose_name='Имя', max_length=100)
    email = models.EmailField(verbose_name='Email', unique=True)

    def __str__(self):
        return self.name


class Bank(models.Model):
    """Банк"""

    name = models.CharField(verbose_name='Название', max_length=100)
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return self.name


class Branch(models.Model):
    """Филиал банка"""

    bank = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE, related_name='branches')
    location = models.CharField(verbose_name='Местоположение', max_length=100)

    def __str__(self):
        return f"{self.bank.name} - {self.location}"


class BankAccount(models.Model):
    """Банковский счет"""

    customer = models.ForeignKey(Customer, verbose_name='Клиент', on_delete=models.CASCADE, related_name='bank_accounts')
    branch = models.ForeignKey(Branch, verbose_name='Филиал', on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(verbose_name='Номер счета', max_length=20, unique=True)
    balance = models.DecimalField(verbose_name='Баланс', max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.name}'s account at {self.branch}"
























































































































































# from django.db import models
# from django.core.validators import MinValueValidator
# from django.conf import settings

# class Currency(models.Model):
#     """Валюта"""

#     symbol = models.CharField(verbose_name='Символ валюты', max_length=2)
#     code = models.CharField(
#         verbose_name='Код валюты',
#         validators=[MinValueValidator(3)],
#         max_length=3,
#         unique=True,
#     )
#     short_name = models.CharField(verbose_name='Краткое название', max_length=3)
#     full_name = models.CharField(verbose_name='Полное название', max_length=50)

#     class Meta:
#         verbose_name = 'Валюта'
#         verbose_name_plural = 'Валюты'

#     def __str__(self):
#         return self.full_name


# class Account(models.Model):
#     """Счет"""

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account')
#     currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.SET_NULL, null=True)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"Account of {self.user.username}"

#     def deposit(self, amount):
#         """Пополнение баланса"""
#         self.balance += amount
#         self.save()

#     def withdraw(self, amount):
#         """Вывод средств"""
#         if self.balance >= amount:
#             self.balance -= amount
#             self.save()
#             return True
#         return False


# class Transaction(models.Model):
#     """Транзакция"""

#     TRANSACTION_TYPES = (
#         ('deposit', 'Пополнение'),
#         ('withdrawal', 'Вывод средств'),
#     )

#     account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.transaction_type} of {self.amount} for account {self.account}"


# class Application(models.Model):
#     """Заявка на ввод/вывод средств"""

#     account = models.ForeignKey(Account, verbose_name='Счет', on_delete=models.SET_NULL, null=True)
#     currency = models.ForeignKey(Currency, verbose_name='Валюта', on_delete=models.SET_NULL, null=True)

#     payment_id = models.UUIDField(verbose_name="Id платежа", unique=True, editable=False, blank=True, null=True)
#     amount = models.DecimalField(
#         verbose_name='Сумма',
#         max_digits=11,
#         decimal_places=2,
#         default=0,
#         validators=[MinValueValidator(0)],
#     )
#     type_ = models.CharField(verbose_name='Тип платежа', choices=Transaction.TRANSACTION_TYPES, max_length=20)
#     status = models.CharField(verbose_name='Статус', max_length=20)

#     def __str__(self):
#         return f"{self.get_type_display()} application of {self.amount} for account {self.account}"


# class ApplicationLog(models.Model):
#     """История изменений заявки"""

#     application = models.ForeignKey(Application, verbose_name='Заявка', on_delete=models.SET_NULL, null=True)

#     status = models.CharField(verbose_name='Статус', max_length=20)

#     def __str__(self):
#         return f"Log for {self.application}: {self.status}"
