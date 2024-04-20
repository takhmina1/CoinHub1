from django.urls import path
from .views import CryptocurrencyListCreateView, PortfolioListCreateView, OrderListCreateView

urlpatterns = [
    path('cryptocurrencies/', CryptocurrencyListCreateView.as_view(), name='cryptocurrency-list-create'),
    path('portfolios/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]



























# from django.urls import path
# from . import views

# urlpatterns = [
#     path('cryptocurrencies/', views.CryptocurrencyListCreateView.as_view(), name='cryptocurrency_list_create'),
#     path('portfolios/', views.PortfolioListCreateView.as_view(), name='portfolio_list_create'),
#     path('orders/', views.OrderListCreateView.as_view(), name='order_list_create'),
# ]























# from django.urls import path
# from .views import CryptocurrencyListCreateView, PortfolioListCreateView, OrderListCreateView

# urlpatterns = [
#     path('cryptocurrencies', CryptocurrencyListCreateView.as_view(), name='cryptocurrency-list-create'),
#     path('portfolios/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
#     path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
# ]
