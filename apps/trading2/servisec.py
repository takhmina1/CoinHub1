from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .models import Transaction
from .currency_converter import CurrencyConverter
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cosine
import numpy as np
from sklearn.cluster import KMeans


class TransactionService:
    @staticmethod
    def perform_transaction(user, transaction_type, amount, currency):
        try:
            # Проверяем баланс пользователя
            balance = TransactionService.check_balance(user)
            if balance is None or balance < amount:
                return False, "Недостаточно средств на счету"
            
            # Создаем новую транзакцию
            transaction = Transaction.objects.create(
                user=user,
                transaction_type=transaction_type,
                amount=amount,
                currency=currency
            )
            return True, transaction
        except Exception as e:
            return False, str(e)

    @staticmethod
    def check_balance(user):
        try:
            # Считаем баланс пользователя как сумму всех его транзакций
            total_balance = Transaction.objects.filter(user=user).aggregate(models.Sum('amount'))['amount__sum']
            return total_balance or 0
        except ObjectDoesNotExist:
            return None



class CurrencyConversionService:
    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        """
        Выполняет конвертацию валюты с использованием CurrencyConverter.

        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Сумма после конвертации в целевой валюте и сообщение об ошибке (если есть).
        """
        return CurrencyConverter.convert_currency(amount, from_currency, to_currency)

    @staticmethod
    def get_supported_currencies():
        """
        Возвращает список поддерживаемых валют.
        """
        return CurrencyConverter.get_supported_currencies()

    @staticmethod
    def get_conversion_rate(from_currency, to_currency):
        """
        Возвращает коэффициент конвертации между двумя валютами.

        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Коэффициент конвертации или None, если конвертация невозможна.
        """
        return CurrencyConverter.get_conversion_rate(from_currency, to_currency)

    @staticmethod
    def perform_transaction(amount, from_currency, to_currency):
        """
        Выполняет транзакцию конвертации валюты.

        :param amount: Сумма для конвертации.
        :param from_currency: Исходная валюта.
        :param to_currency: Целевая валюта.
        :return: Словарь с результатом транзакции, включая сконвертированную сумму и статус операции.
        """
        converted_amount, error_message = CurrencyConverter.convert_currency(amount, from_currency, to_currency)
        if error_message:
            return {'success': False, 'error_message': error_message}
        else:
            return {'success': True, 'converted_amount': converted_amount}

  

class TransactionAnalyzer:
    @staticmethod
    def find_anomalies(transactions):
        """
        Находит аномалии в транзакциях с использованием анализа временных рядов и кластеризации.

        :param transactions: Список транзакций для анализа.
        :return: Список аномальных транзакций.
        """
        # Извлекаем временные метки и суммы транзакций
        timestamps = [transaction.timestamp for transaction in transactions]
        amounts = [transaction.amount for transaction in transactions]

        # Нормализуем данные
        X = np.column_stack((timestamps, amounts))
        X = StandardScaler().fit_transform(X)

        # Кластеризуем транзакции по временным меткам и суммам
        dbscan = DBSCAN(eps=0.5, min_samples=5, metric=cosine)
        dbscan.fit(X)

        # Ищем аномальные кластеры
        labels = dbscan.labels_
        unique_labels = set(labels)
        anomalies = []
        for label in unique_labels:
            if label == -1:  # Кластер аномалий
                cluster_indices = np.where(labels == label)[0]
                cluster_transactions = [transactions[i] for i in cluster_indices]
                anomalies.extend(cluster_transactions)

        return anomalies



class TransactionAnalyzer:
    @staticmethod
    def analyze_transaction_trend(transactions):
        """
        Анализирует тренд транзакций для выявления аномалий.

        :param transactions: Список транзакций для анализа.
        :return: Список аномальных транзакций по тренду.
        """
        # Получаем суммы транзакций
        transaction_amounts = [transaction.amount for transaction in transactions]

        # Вычисляем скользящее среднее с окном 5
        moving_average = np.convolve(transaction_amounts, np.ones(5) / 5, mode='valid')

        # Вычисляем стандартное отклонение для сумм транзакций
        std_deviation = np.std(transaction_amounts)

        # Определяем верхний порог аномалий (mean + 2 * std_dev)
        anomaly_threshold = np.mean(transaction_amounts) + 2 * std_deviation

        # Находим аномальные транзакции
        anomalies = [transactions[i] for i, amount in enumerate(transaction_amounts) if amount > anomaly_threshold]

        return anomalies


class TransactionAnalyzer:
    @staticmethod
    def cluster_transactions(transactions):
        """
        Кластеризует транзакции для выявления аномалий.

        :param transactions: Список транзакций для кластеризации.
        :return: Список аномальных транзакций по кластерам.
        """
        # Преобразование признаков транзакций для кластеризации
        transaction_features = [[transaction.amount, transaction.timestamp] for transaction in transactions]

        # Количество кластеров
        num_clusters = 3

        # Кластеризация методом k-средних
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(transaction_features)
        labels = kmeans.labels_

        # Выбираем центры кластеров
        cluster_centers = kmeans.cluster_centers_

        # Определяем аномальные транзакции как те, которые находятся далеко от центров кластеров
        anomalies = [transactions[i] for i, label in enumerate(labels) if np.linalg.norm(transaction_features[i] - cluster_centers[label]) > 2]

        return anomalies


