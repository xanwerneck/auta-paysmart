from django.urls import path
from generic import api as api_generic
from transacao import api as api_transacao

urlpatterns = [
 path('status', api_generic.StatusApi.as_view()),
 path('purchases', api_transacao.CompraApi.as_view()),
 path('purchases/cancel', api_transacao.CancelamentoCompraApi.as_view()),
 path('chargebacks', api_transacao.EstornoCompraApi.as_view()),
 path('queries', api_transacao.SaldoApi.as_view())
]