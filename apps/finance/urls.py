from django.urls import path
from .views import AccountBalanceView, DepositView, WithdrawView, TransactionHistoryView

urlpatterns = [
    path('account/<int:account_id>/balance/', AccountBalanceView.as_view(), name='account_balance'),
    path('deposit/', DepositView.as_view(), name='deposit'),
    path('withdraw/', WithdrawView.as_view(), name='withdraw'),
    path('account/<int:account_id>/transactions/', TransactionHistoryView.as_view(), name='transaction_history'),
]















# from django.urls import path
# from .views import AccountBalanceView, DepositView, WithdrawalView, TransactionHistoryView

# urlpatterns = [
#     path('balance/', AccountBalanceView.as_view(), name='balance'),
#     path('deposit/', DepositView.as_view(), name='deposit'),
#     path('withdraw/', WithdrawalView.as_view(), name='withdraw'),
#     path('transactions/', TransactionHistoryView.as_view(), name='transactions'),
# ]

