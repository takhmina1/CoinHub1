from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# from apps.finance.services import AccountService, TransactionService
from apps.finance.services import AccountService


class AccountBalanceView(APIView):
    @swagger_auto_schema(
        operation_description="Просмотр баланса счета",
        responses={200: "Баланс счета", 404: "Счет не найден"}
    )
    def get(self, request, account_id):
        balance = AccountService.get_account_balance(account_id)
        if balance is not None:
            return Response({"balance": balance}, status=status.HTTP_200_OK)
        return Response({"message": "Счет не найден"}, status=status.HTTP_404_NOT_FOUND)

class DepositView(APIView):
    @swagger_auto_schema(
        operation_description="Пополнение баланса",
        responses={200: "Счет успешно пополнен", 400: "Недопустимая сумма"}
    )
    def post(self, request):
        account_id = request.data.get("account_id")
        amount = request.data.get("amount")
        if account_id and amount:
            if AccountService.deposit(account_id, amount):
                return Response({"message": "Счет успешно пополнен"}, status=status.HTTP_200_OK)
            return Response({"message": "Недопустимая сумма"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Отсутствуют обязательные параметры"}, status=status.HTTP_400_BAD_REQUEST)

class WithdrawView(APIView):
    @swagger_auto_schema(
        operation_description="Вывод средств",
        responses={200: "Средства успешно выведены", 400: "Недостаточно средств"}
    )
    def post(self, request):
        account_id = request.data.get("account_id")
        amount = request.data.get("amount")
        if account_id and amount:
            if AccountService.withdraw(account_id, amount):
                return Response({"message": "Средства успешно выведены"}, status=status.HTTP_200_OK)
            return Response({"message": "Недостаточно средств"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Отсутствуют обязательные параметры"}, status=status.HTTP_400_BAD_REQUEST)

class TransactionHistoryView(APIView):
    @swagger_auto_schema(
        operation_description="История транзакций",
        responses={200: "История транзакций", 404: "Счет не найден"}
    )
    def get(self, request, account_id):
        transactions = TransactionService.get_transaction_history(account_id)
        if transactions is not None:
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Счет не найден"}, status=status.HTTP_404_NOT_FOUND)




























































































# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from .models import Account, Transaction
# from .serializers import AccountSerializer, TransactionSerializer

# class AccountBalanceView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         account = request.user.account
#         serializer = AccountSerializer(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class DepositView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         amount = request.data.get('amount')
#         if amount:
#             account = request.user.account
#             account.balance += amount
#             account.save()
#             transaction = Transaction.objects.create(
#                 account=account,
#                 amount=amount,
#                 transaction_type='deposit',
#                 description='Deposit transaction'
#             )
#             serializer = TransactionSerializer(transaction)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# class WithdrawalView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         amount = request.data.get('amount')
#         if amount:
#             account = request.user.account
#             if account.balance >= amount:
#                 account.balance -= amount
#                 account.save()
#                 transaction = Transaction.objects.create(
#                     account=account,
#                     amount=amount,
#                     transaction_type='withdrawal',
#                     description='Withdrawal transaction'
#                 )
#                 serializer = TransactionSerializer(transaction)
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

# class TransactionHistoryView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         account = request.user.account
#         transactions = Transaction.objects.filter(account=account).order_by('-timestamp')
#         serializer = TransactionSerializer(transactions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)







































































"""
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import get_account_balance, deposit, withdraw, get_transaction_history

class AccountBalanceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        balance = get_account_balance(request.user)
        if balance is not None:
            return Response({'balance': balance}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

class DepositView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        amount = request.data.get('amount')
        if amount:
            response = deposit(request.user, amount)
            if response['success']:
                return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

class WithdrawalView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        amount = request.data.get('amount')
        if amount:
            response = withdraw(request.user, amount)
            if response['success']:
                return Response({'message': response['message']}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)

class TransactionHistoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = get_transaction_history(request.user)
        if response['success']:
            return Response({'transactions': response['transactions']}, status=status.HTTP_200_OK)
        else:
            return Response({'error': response['error']}, status=status.HTTP_400_BAD_REQUEST)




"""