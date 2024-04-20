from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Currency, Account, Transaction, Application, ApplicationLog, Customer, Bank, Branch, BankAccount


class CurrencySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Currency.

    Включает бизнес-логику для проверки уникальности кода валюты и для проверки допустимых символов.
    """

    class Meta:
        model = Currency
        fields = ['id', 'symbol', 'code', 'short_name', 'full_name']

    def validate_code(self, value):
        """
        Проверка уникальности кода валюты.

        Проверяет, что код валюты уникален в пределах всех существующих валют.
        """
        existing_currency = Currency.objects.filter(code=value).exists()
        if existing_currency:
            raise serializers.ValidationError("Валюта с таким кодом уже существует")
        return value

    def validate_symbol(self, value):
        """
        Проверка допустимых символов в символе валюты.

        Проверяет, что символ валюты состоит ровно из двух букв.
        """
        if len(value) != 2 or not value.isalpha():
            raise serializers.ValidationError("Символ валюты должен состоять ровно из двух букв")
        return value





class CustomerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Customer"""

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email']

    def create(self, validated_data):
        """
        Создание нового клиента.

        Проверяет уникальность email и создает нового клиента, если email уникален.
        """
        email = validated_data.get('email')
        existing_customer = Customer.objects.filter(email=email).exists()
        if existing_customer:
            raise serializers.ValidationError("Клиент с таким email уже существует")
        
        customer = Customer.objects.create(**validated_data)
        return customer

    def update(self, instance, validated_data):
        """
        Обновление информации о клиенте.

        Позволяет обновлять данные клиента, в том числе email.
        """
        # Проверяем, что новый email не совпадает с email других клиентов
        if 'email' in validated_data:
            new_email = validated_data['email']
            existing_customer = Customer.objects.exclude(pk=instance.pk).filter(email=new_email).exists()
            if existing_customer:
                raise serializers.ValidationError("Клиент с таким email уже существует")

        # Обновляем данные клиента
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance




class BankSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Bank"""

    class Meta:
        model = Bank
        fields = ['id', 'name', 'address']

    def create(self, validated_data):
        """
        Создание нового банка.

        Проверяет уникальность названия банка и создает новый банк, если название уникально.
        """
        name = validated_data.get('name')
        existing_bank = Bank.objects.filter(name=name).exists()
        if existing_bank:
            raise serializers.ValidationError("Банк с таким названием уже существует")
        
        bank = Bank.objects.create(**validated_data)
        return bank

    def update(self, instance, validated_data):
        """
        Обновление информации о банке.

        Позволяет обновлять данные о банке, в том числе его название и адрес.
        """
        # Проверяем, что новое название банка не совпадает с названием других банков
        if 'name' in validated_data:
            new_name = validated_data['name']
            existing_bank = Bank.objects.exclude(pk=instance.pk).filter(name=new_name).exists()
            if existing_bank:
                raise serializers.ValidationError("Банк с таким названием уже существует")

        # Обновляем данные о банке
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance




class BranchSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Branch"""

    class Meta:
        model = Branch
        fields = ['id', 'bank', 'location']

    def create(self, validated_data):
        """
        Создание нового филиала банка.

        Проверяет, что филиал с таким местоположением не существует в данном банке,
        и создает новый филиал, если условие выполнено.
        """
        bank = validated_data.get('bank')
        location = validated_data.get('location')
        existing_branch = Branch.objects.filter(bank=bank, location=location).exists()
        if existing_branch:
            raise serializers.ValidationError("Филиал с таким местоположением уже существует для этого банка")

        branch = Branch.objects.create(**validated_data)
        return branch

    def update(self, instance, validated_data):
        """
        Обновление информации о филиале банка.

        Позволяет обновлять данные о филиале банка, в том числе местоположение.
        """
        # Проверяем, что новое местоположение не совпадает с местоположением других филиалов этого банка
        if 'location' in validated_data:
            new_location = validated_data['location']
            existing_branch = Branch.objects.exclude(pk=instance.pk).filter(bank=instance.bank, location=new_location).exists()
            if existing_branch:
                raise serializers.ValidationError("Филиал с таким местоположением уже существует для этого банка")

        # Обновляем данные о филиале банка
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance



class BankAccountSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели BankAccount.

    Позволяет создавать и обновлять банковские счета, а также проверяет уникальность номера счета
    и отрицательность баланса.
    """

    class Meta:
        model = BankAccount
        fields = ['id', 'customer', 'branch', 'account_number', 'balance']

    def create(self, validated_data):
        """
        Создание нового банковского счета.

        Проверяет уникальность номера счета и создает новый счет, если номер уникален.
        """
        existing_account = BankAccount.objects.filter(account_number=validated_data['account_number']).exists()
        if existing_account:
            raise ValidationError("Банковский счет с таким номером уже существует")
        
        bank_account = BankAccount.objects.create(**validated_data)
        return bank_account

    def update(self, instance, validated_data):
        """
        Обновление информации о банковском счете.

        Проверяет отрицательность нового баланса и сохраняет обновленную информацию о счете.
        """
        new_balance = validated_data.get('balance')
        if new_balance is not None and new_balance < 0:
            raise ValidationError("Баланс не может быть отрицательным")
        
        instance.balance = new_balance
        instance.save()
        return instance




class AccountSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Account"""

    balance = serializers.SerializerMethodField()  # Добавляем поле для баланса

    class Meta:
        model = Account
        fields = ['id', 'user', 'currency', 'balance']

    def get_balance(self, obj):
        """Метод для просмотра баланса счета."""
        return obj.balance

    def validate_balance(self, value):
        """
        Валидация баланса счета.

        Проверяет, что значение баланса не отрицательное.
        """
        if value < 0:
            raise serializers.ValidationError("Баланс не может быть отрицательным")
        return value

    def deposit(self, instance, amount):
        """Метод для пополнения баланса счета."""
        instance.balance += amount
        instance.save()
        # Создание записи о транзакции
        Transaction.objects.create(account=instance, amount=amount, transaction_type='deposit')

    def withdraw(self, instance, amount):
        """Метод для вывода средств."""
        if instance.balance >= amount:
            instance.balance -= amount
            instance.save()
            # Создание записи о транзакции
            Transaction.objects.create(account=instance, amount=amount, transaction_type='withdrawal')
            return True
        return False




class TransactionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Transaction"""

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'transaction_type', 'timestamp', 'description']

    def create(self, validated_data):
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




class ApplicationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Application"""

    class Meta:
        model = Application
        fields = ['id', 'account', 'currency', 'payment_id', 'amount', 'type_', 'status']

    def create(self, validated_data):
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
            raise serializers.ValidationError("Insufficient funds for the application")

    def update(self, instance, validated_data):
        """
        Обновление заявки.

        Добавляем бизнес-логику для обновления заявки,
        например, обновление статуса и отправка уведомления о изменении.
        """
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

    def cancel_application(self, instance):
        """
        Отмена заявки.

        Добавляем возможность отмены заявки.
        """
        instance.status = 'canceled'
        instance.save()
        return instance

    def approve_application(self, instance):
        """
        Подтверждение заявки.

        Добавляем возможность подтверждения заявки.
        """
        instance.status = 'approved'
        instance.save()
        return instance



class ApplicationLogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ApplicationLog"""

    class Meta:
        model = ApplicationLog
        fields = ['id', 'application', 'status']

    def create(self, validated_data):
        """
        Создание истории изменений заявки.

        Добавляем бизнес-логику для создания истории изменений заявки.
        """
        application_log = ApplicationLog.objects.create(**validated_data)
        return application_log

    def update_status(self, instance, new_status):
        """
        Обновление статуса истории изменений заявки.

        Добавляем возможность обновления статуса истории изменений заявки.
        """
        instance.status = new_status
        instance.save()
        return instance
