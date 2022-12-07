from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.WalletDetailsView.as_view(), name='wallet_details'),
    path('add-credit', views.AddCreditToWallet.as_view(), name='add_credit_to_wallet'),
    path('debit-amount', views.DebitAmountFromWallet.as_view(), name='debit_amount_from_wallet'),

]
