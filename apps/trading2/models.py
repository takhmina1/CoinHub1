from django.db import models
from django.db.models import Sum, Avg, Min, Max
from datetime import datetime, timedelta
from statistics import stdev, mean
from .currency_converter import conversion_rates

# from .currency_converter import conversion_rates


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('BUY', 'Покупка'),
        ('SELL', 'Продажа'),
        ('EXCHANGE', 'Обмен'),
    )

    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def filter_by_date_range(start_date, end_date, user):
        """
        Фильтрация транзакций по диапазону дат
        """
        return Transaction.objects.filter(timestamp__range=(start_date, end_date), user=user)

    @staticmethod
    def delete_transaction(transaction_id):
        """
        Удаление транзакции по идентификатору
        """
        try:
            transaction = Transaction.objects.get(pk=transaction_id)
            transaction.delete()
            return True
        except Transaction.DoesNotExist:
            return False

    @staticmethod
    def update_transaction(transaction_id, new_amount):
        """
        Обновление данных о существующей транзакции
        """
        try:
            transaction = Transaction.objects.get(pk=transaction_id)
            transaction.amount = new_amount
            transaction.save()
            return True
        except Transaction.DoesNotExist:
            return False

    @staticmethod
    def count_transactions(user=None, transaction_type=None):
        """
        Подсчет количества транзакций
        """
        query = Transaction.objects.all()
        if user:
            query = query.filter(user=user)
        if transaction_type:
            query = query.filter(transaction_type=transaction_type)
        return query.count()

    @staticmethod
    def get_last_transaction(user):
        """
        Получение информации о последней совершенной транзакции
        """
        try:
            return Transaction.objects.filter(user=user).latest('timestamp')
        except Transaction.DoesNotExist:
            return None

    @staticmethod
from .currency_converter import conversion_rates
    def filter_transactions(**kwargs):
        """
        Фильтрация транзакций по различным параметрам
        """
        return Transaction.objects.filter(**kwargs)


    @staticmethod
    def filter_transactions(**kwargs):
        """
        Фильтрация транзакций по различным параметрам
        """
        return Transaction.objects.filter(**kwargs)




    @staticmethod
    def calculate_total_amount(start_date, end_date):
        """
        Вычисляет общую сумму транзакций за определенный период времени.
        """
        total_amount = Transaction.objects.filter(timestamp__range=(start_date, end_date)).aggregate(Sum('amount'))
        return total_amount['amount__sum'] or 0

    @staticmethod
    def calculate_average_amount(start_date, end_date):
        """
        Вычисляет среднюю сумму транзакций за определенный период времени.
        """
        average_amount = Transaction.objects.filter(timestamp__range=(start_date, end_date)).aggregate(Avg('amount'))
        return average_amount['amount__avg'] or 0

    @staticmethod
    def find_min_max_amount(start_date, end_date):
        """
        Находит минимальное и максимальное значения суммы транзакций за определенный период времени.
        """
        min_max_amount = Transaction.objects.filter(timestamp__range=(start_date, end_date)).aggregate(Min('amount'), Max('amount'))
        return min_max_amount['amount__min'] or 0, min_max_amount['amount__max'] or 0

    @staticmethod
    def filter_by_transaction_type(transaction_type):
        """
        Фильтрует транзакции по типу (покупка, продажа, обмен).
        """
        return Transaction.objects.filter(transaction_type=transaction_type)

    @staticmethod
    def group_by_transaction_type():
        """
        Группирует транзакции по типу (покупка, продажа, обмен).
        """
        return Transaction.objects.values('transaction_type').annotate(total_transactions=Count('id'))



    @staticmethod
    def analyze_transaction_trend():
        """
        Анализирует тренд транзакций.
        """
        # Получение текущей даты
        today = datetime.now().date()

        # Определение периода для анализа (например, последние 30 дней)
        start_date = today - timedelta(days=30)

        # Фильтрация транзакций за указанный период
        transactions = Transaction.objects.filter(date__gte=start_date, date__lte=today)

        # Вычисление суммы транзакций за каждый день
        daily_totals = {}
        for transaction in transactions:
            transaction_date = transaction.date
            if transaction_date in daily_totals:
                daily_totals[transaction_date] += transaction.amount
            else:
                daily_totals[transaction_date] = transaction.amount

        # Анализ тренда: определение роста, падения или стабильности транзакций
        trend = "стабильный"
        if len(daily_totals) > 1:
            prev_day_total = None
            for day, total in daily_totals.items():
                if prev_day_total is not None:
                    if total > prev_day_total:
                        trend = "рост"
                    elif total < prev_day_total:
                        trend = "падение"
                    # Если тотал равен предыдущему, оставляем тренд неизменным
                prev_day_total = total

        return trend


    @staticmethod
    def find_anomalies():
        """
        Находит аномалии в транзакциях.
        """
        # Получение всех транзакций
        transactions = Transaction.objects.all()

        # Создание списка сумм транзакций
        amounts = [transaction.amount for transaction in transactions]

        # Вычисление среднего значения и стандартного отклонения
        mean_amount = mean(amounts)
        std_deviation = stdev(amounts)

        # Определение порогового значения для аномалий
        threshold = mean_amount + 3 * std_deviation

        # Поиск аномальных транзакций
        anomalies = [transaction for transaction in transactions if transaction.amount > threshold]

        return anomalies


    @staticmethod
    def get_user_transactions(user):
        """
        Получает список транзакций пользователя.
        """
        # Получение списка всех транзакций пользователя
        user_transactions = Transaction.objects.filter(user=user)

        # Вычисление общей суммы всех транзакций пользователя
        total_amount = user_transactions.aggregate(total=Sum('amount'))['total']

        # Вычисление средней суммы транзакции пользователя
        if total_amount:
            average_amount = total_amount / len(user_transactions)
        else:
            average_amount = 0

        # Поиск самой большой и самой маленькой транзакции пользователя
        if user_transactions.exists():
            max_transaction = user_transactions.order_by('-amount').first()
            min_transaction = user_transactions.order_by('amount').first()
        else:
            max_transaction = None
            min_transaction = None

        return {
            'transactions': user_transactions,
            'total_amount': total_amount,
            'average_amount': average_amount,
            'max_transaction': max_transaction,
            'min_transaction': min_transaction
        }
        
        

class CurrencyConverter:
    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        """
        Конвертирует сумму транзакции из одной валюты в другую.

        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Сумма после конвертации в целевой валюте и сообщение об ошибке (если есть).
        """
        if from_currency == to_currency:
            return amount, None

        if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
            return None, "Конвертация между этими валютами невозможна"

        # Получение коэффициента конвертации
        conversion_rate = conversion_rates[from_currency][to_currency]

        # Выполнение конвертации
        converted_amount = amount * conversion_rate

        return converted_amount, None

    @staticmethod
    def get_supported_currencies():
        """
        Возвращает список поддерживаемых валют.
        """
        return list(conversion_rates.keys())

    @staticmethod
    def get_conversion_rate(from_currency, to_currency):
        """
        Возвращает коэффициент конвертации между двумя валютами.

        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Коэффициент конвертации или None, если конвертация невозможна.
        """
        if from_currency == to_currency:
            return 1.0

        if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
            return None

        return conversion_rates[from_currency][to_currency]



