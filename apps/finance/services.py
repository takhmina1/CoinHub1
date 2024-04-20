from .models import Currency

class CurrencyService:
    @staticmethod
    def is_unique_code(code):
        """
        Проверка уникальности кода валюты.

        Проверяет, что код валюты уникален в пределах всех существующих валют.
        """
        return not Currency.objects.filter(code=code).exists()

    @staticmethod
    def is_valid_symbol(symbol):
        """
        Проверка допустимых символов в символе валюты.

        Проверяет, что символ валюты состоит ровно из двух букв.
        """
        return len(symbol) == 2 and symbol.isalpha()

    @staticmethod
    def is_valid_short_name(short_name):
        """
        Проверка допустимости короткого названия валюты.

        Проверяет, что короткое название состоит ровно из трех букв.
        """
        return len(short_name) == 3 and short_name.isalpha()

    @staticmethod
    def is_valid_full_name(full_name):
        """
        Проверка допустимости полного названия валюты.

        Проверяет, что полное название валюты не пустое и не превышает 50 символов.
        """
        return full_name and len(full_name) <= 50

    @staticmethod
    def create_currency(symbol, code, short_name, full_name):
        """
        Создание новой валюты.

        Создает новый объект валюты с заданными параметрами, если они прошли проверку.
        """
        if CurrencyService.is_unique_code(code) and \
                CurrencyService.is_valid_symbol(symbol) and \
                CurrencyService.is_valid_short_name(short_name) and \
                CurrencyService.is_valid_full_name(full_name):
            currency = Currency.objects.create(symbol=symbol, code=code, short_name=short_name, full_name=full_name)
            return currency
        else:
            raise ValueError("Неверные данные для создания валюты")

    @staticmethod
    def update_currency(currency, symbol, code, short_name, full_name):
        """
        Обновление существующей валюты.

        Обновляет существующий объект валюты с заданными параметрами, если они прошли проверку.
        """
        if CurrencyService.is_unique_code(code) and \
                CurrencyService.is_valid_symbol(symbol) and \
                CurrencyService.is_valid_short_name(short_name) and \
                CurrencyService.is_valid_full_name(full_name):
            currency.symbol = symbol
            currency.code = code
            currency.short_name = short_name
            currency.full_name = full_name
            currency.save()
            return currency
        else:
            raise ValueError("Неверные данные для обновления валюты")




from .models import Customer

class CustomerService:
    @staticmethod
    def is_unique_email(email):
        """
        Проверка уникальности email.

        Проверяет, что email уникален в пределах всех существующих клиентов.
        """
        return not Customer.objects.filter(email=email).exists()

    @staticmethod
    def create_customer(name, email):
        """
        Создание нового клиента.

        Создает нового клиента с заданными параметрами, если email уникален.
        """
        if CustomerService.is_unique_email(email):
            customer = Customer.objects.create(name=name, email=email)
            return customer
        else:
            raise ValueError("Клиент с таким email уже существует")

    @staticmethod
    def update_customer(customer, name, email):
        """
        Обновление информации о клиенте.

        Обновляет информацию о существующем клиенте с заданными параметрами, если email уникален.
        """
        if CustomerService.is_unique_email(email):
            customer.name = name
            customer.email = email
            customer.save()
            return customer
        else:
            raise ValueError("Клиент с таким email уже существует")




from .models import Bank

class BankService:
    @staticmethod
    def is_unique_name(name):
        """
        Проверка уникальности названия банка.

        Проверяет, что название банка уникально в пределах всех существующих банков.
        """
        return not Bank.objects.filter(name=name).exists()

    @staticmethod
    def create_bank(name, address):
        """
        Создание нового банка.

        Создает новый банк с заданными параметрами, если название уникально.
        """
        if BankService.is_unique_name(name):
            bank = Bank.objects.create(name=name, address=address)
            return bank
        else:
            raise ValueError("Банк с таким названием уже существует")

    @staticmethod
    def update_bank(bank, name, address):
        """
        Обновление информации о банке.

        Обновляет информацию о существующем банке с заданными параметрами, если название уникально.
        """
        if BankService.is_unique_name(name):
            bank.name = name
            bank.address = address
            bank.save()
            return bank
        else:
            raise ValueError("Банк с таким названием уже существует")




from .models import Branch

class BranchService:
    @staticmethod
    def is_unique_location_for_bank(bank, location):
        """
        Проверка уникальности местоположения филиала для данного банка.

        Проверяет, что филиал с указанным местоположением уникален для данного банка.
        """
        return not Branch.objects.filter(bank=bank, location=location).exists()

    @staticmethod
    def create_branch(bank, location):
        """
        Создание нового филиала банка.

        Создает новый филиал для указанного банка с заданным местоположением,
        если местоположение уникально для данного банка.
        """
        if BranchService.is_unique_location_for_bank(bank, location):
            branch = Branch.objects.create(bank=bank, location=location)
            return branch
        else:
            raise ValueError("Филиал с таким местоположением уже существует для этого банка")

    @staticmethod
    def update_branch(branch, location):
        """
        Обновление информации о филиале банка.

        Обновляет информацию о существующем филиале банка с заданным местоположением,
        если местоположение уникально для данного банка.
        """
        if BranchService.is_unique_location_for_bank(branch.bank, location):
            branch.location = location
            branch.save()
            return branch
        else:
            raise ValueError("Филиал с таким местоположением уже существует для этого банка")




from .models import BankAccount

class BankAccountService:
    @staticmethod
    def is_unique_account_number(account_number):
        """
        Проверка уникальности номера банковского счета.

        Проверяет, что банковский счет с указанным номером уникален.
        """
        return not BankAccount.objects.filter(account_number=account_number).exists()

    @staticmethod
    def create_bank_account(customer, branch, account_number, balance):
        """
        Создание нового банковского счета.

        Создает новый банковский счет с указанными параметрами,
        если номер счета уникален.
        """
        if BankAccountService.is_unique_account_number(account_number):
            bank_account = BankAccount.objects.create(customer=customer, branch=branch, account_number=account_number, balance=balance)
            return bank_account
        else:
            raise ValueError("Банковский счет с таким номером уже существует")

    @staticmethod
    def update_bank_account(bank_account, balance):
        """
        Обновление информации о банковском счете.

        Обновляет баланс существующего банковского счета с указанным номером,
        если новый баланс не отрицательный.
        """
        if balance is not None and balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        
        bank_account.balance = balance
        bank_account.save()
        return bank_account




from .models import Account, Transaction

class AccountService:
    @staticmethod
    def deposit(account, amount):
        """
        Пополнение баланса счета.

        Пополняет баланс указанного счета на указанную сумму и создает запись о транзакции.
        """
        account.balance += amount
        account.save()
        # Создание записи о транзакции
        Transaction.objects.create(account=account, amount=amount, transaction_type='deposit')

    @staticmethod
    def withdraw(account, amount):
        """
        Вывод средств.

        Проверяет наличие достаточных средств на счете, вычитает указанную сумму из баланса и
        создает запись о транзакции, если операция выполнена успешно.
        """
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            # Создание записи о транзакции
            Transaction.objects.create(account=account, amount=amount, transaction_type='withdrawal')
            return True
        return False




from .models import Transaction

class TransactionService:
    @staticmethod
    def create_transaction(validated_data):
        """
        Создание транзакции.

        При создании транзакции также обновляется баланс счета,
        к которому относится транзакция.
        """
        transaction = Transaction.objects.create(**validated_data)
        
        # Обновление баланса счета в зависимости от типа транзакции
        account = transaction.account
        if transaction.transaction_type == 'deposit':
            account.balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            # Проверяем, достаточно ли средств на счету для выполнения транзакции вывода
            if account.balance >= transaction.amount:
                account.balance -= transaction.amount
            else:
                # Если недостаточно средств, возбуждаем исключение
                raise serializers.ValidationError("Insufficient funds for withdrawal")
        account.save()

        return transaction




from .models import Application

class ApplicationService:
    @staticmethod
    def create_application(validated_data):
        """
        Создание заявки.

        При создании заявки проверяется доступность средств на счете
        перед созданием заявки.
        """
        account = validated_data.get('account')
        amount = validated_data.get('amount')

        # Проверяем, достаточно ли средств на счете для создания заявки
        if account.balance >= amount:
            application = Application.objects.create(**validated_data)
            return application
        else:
            # Если недостаточно средств, возбуждаем исключение
            raise ValueError("Insufficient funds for the application")

    @staticmethod
    def update_application(instance, validated_data):
        """
        Обновление заявки.

        Добавляем бизнес-логику для обновления заявки,
        например, обновление статуса и отправка уведомления о изменении.
        """
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    @staticmethod
    def cancel_application(instance):
        """
        Отмена заявки.

        Добавляем возможность отмены заявки.
        """
        instance.status = 'canceled'
        instance.save()
        return instance

    @staticmethod
    def approve_application(instance):
        """
        Подтверждение заявки.

        Добавляем возможность подтверждения заявки.
        """
        instance.status = 'approved'
        instance.save()
        return instance





from .models import ApplicationLog

class ApplicationLogService:
    @staticmethod
    def create_application_log(validated_data):
        """
        Создание истории изменений заявки.

        Добавляем бизнес-логику для создания истории изменений заявки.
        """
        application_log = ApplicationLog.objects.create(**validated_data)
        return application_log

    @staticmethod
    def update_status(instance, new_status):
        """
        Обновление статуса истории изменений заявки.

        Добавляем возможность обновления статуса истории изменений заявки.
        """
        instance.status = new_status
        instance.save()
        return instance






















































































# from .models import Account, Transaction, Application

# class AccountService:
#     @staticmethod
#     def get_account_balance(account_id):
#         """Получить баланс счета"""
#         try:
#             account = Account.objects.get(pk=account_id)
#             return account.balance
#         except Account.DoesNotExist:
#             return None

#     @staticmethod
#     def deposit(account_id, amount):
#         """Пополнить счет"""
#         try:
#             account = Account.objects.get(pk=account_id)
#             account.balance += amount
#             account.save()
#             Transaction.objects.create(
#                 account=account,
#                 amount=amount,
#                 transaction_type=Transaction.DEPOSIT
#             )
#             return True
#         except Account.DoesNotExist:
#             return False

#     @staticmethod
#     def withdraw(account_id, amount):
#         """Вывести средства со счета"""
#         try:
#             account = Account.objects.get(pk=account_id)
#             if account.balance >= amount:
#                 account.balance -= amount
#                 account.save()
#                 Transaction.objects.create(
#                     account=account,
#                     amount=amount,
#                     transaction_type=Transaction.WITHDRAWAL
#                 )
#                 return True
#             return False
#         except Account.DoesNotExist:
#             return False

#     @staticmethod
#     def create_application(account_id, currency_id, amount, application_type):
#         """Создать заявку на ввод/вывод средств"""
#         try:
#             account = Account.objects.get(pk=account_id)
#             currency = Currency.objects.get(pk=currency_id)
#             application = Application.objects.create(
#                 account=account,
#                 currency=currency,
#                 amount=amount,
#                 type=application_type,
#                 status=Application.PENDING
#             )
#             return application
#         except (Account.DoesNotExist, Currency.DoesNotExist):
#             return None


















































































































# # from rest_framework import status
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework.permissions import IsAuthenticated
# # from .services import get_account_balance, deposit, withdraw, get_transaction_history

# # class AccountBalanceView(APIView):
# #     permission_classes = (IsAuthenticated,)

# #     def get(self, request):
# #         balance = get_account_balance(request.user)
# #         if balance is not None:
# #             return Response({'balance': balance}, status=status.HTTP_200_OK)
# #         else:
# #             return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

# # class DepositView(APIView):
# #     permission_classes = (IsAuthenticated,)

# #     def post(self, request):
# #         amount = request.data.get('amount')
# #         if amount:
# #             response = deposit(request.user, amount)
# #             if response['success']:
# #                 return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
# #             else:
# #                 return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# # class WithdrawalView(APIView):
# #     permission_classes = (IsAuthenticated,)

# #     def post(self, request):
# #         amount = request.data.get('amount')
# #         if amount:
# #             response = withdraw(request.user, amount)
# #             if response['success']:
# #                 return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
# #             else:
# #                 return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
# #         else:
# #             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# # class TransactionHistoryView(APIView):
# #     permission_classes = (IsAuthenticated,)

# #     def get(self, request):
# #         response = get_transaction_history(request.user)
# #         if response['success']:
# #             return Response({'transactions': response['transactions']}, status=status.HTTP_200_OK)
# #         else:
# #             return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
