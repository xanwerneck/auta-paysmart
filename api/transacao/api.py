from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from generic.api import AuthenticatedView, NotAuthenticatedView
from django.http.response import JsonResponse
from rest_framework import status
from transacao.models import *
from transacao.serializers import CompraSerializer, StatusCompraSerializer
import uuid

class CompraApi(AuthenticatedView):    
    def post(self, request):
        data  = JSONParser().parse(request)
        status_code = data['authorization']['code']
        if status_code == "00":
            #TO DO - begin transaction

            # atualizar saldo
            conta = Conta.objects.get(account_id_paysmart=data['account_id'])

            conta_corrente = ContaCorrente.objects.get(conta=conta)
            amount_transaction = (float(data['total_amount']['amount']) / 100)
            if conta_corrente.saldo <= amount_transaction:
                return JsonResponse(data={"descricao" : "Saldo insuficiente"}, safe=False, status=status.HTTP_400_BAD_REQUEST) 

            conta_corrente.saldo -= amount_transaction
            conta_corrente.save()

            transacao = Transacao()
            transacao.authorization_id = uuid.uuid4().hex[:6].upper()
            transacao.obs = "Transacao realizada pela PAYSmart"
            transacao.conta = conta_corrente
            transacao.save()

            # TO DO - end transaction 

            # retornar a confirmacao
            return JsonResponse(data={
                "message": "Operação realizada com sucesso.",
                "code": 0,
                "authorization_id": transacao.pk,
                "balance": {
                    "amount": int(conta_corrente.saldo * 100),
                    "currency_code": 986
                }
            }, safe=False) 
                
            
        return JsonResponse(data=None, safe=False, status=499)


class CancelamentoCompraApi(AuthenticatedView): 
    def post(self, request):
        data  = JSONParser().parse(request)
        status_code = data['authorization']['code']
        if status_code == "00":
            #TO DO - begin transaction

            # atualizar saldo
            conta = Conta.objects.get(account_id_paysmart=data['account_id'])

            conta_corrente = ContaCorrente.objects.get(conta=conta)
            amount_transaction = (float(data['original_amount']['amount']) / 100)
            conta_corrente.saldo += amount_transaction
            conta_corrente.save()

            transacao = Transacao()
            transacao.authorization_id = uuid.uuid4().hex[:6].upper()
            transacao.obs = "Transacao de cancelamento realizada pela PAYSmart"
            transacao.conta = conta_corrente
            transacao.save()

            # TO DO - end transaction 

            # retornar a confirmacao
            return JsonResponse(data={
                "message": "Operação realizada com sucesso.",
                "code": 0,
                "authorization_id": transacao.pk,
                "balance": {
                    "amount": int(conta_corrente.saldo * 100),
                    "currency_code": 986
                }
            }, safe=False) 
                
            
        return JsonResponse(data=None, safe=False, status=499)

class EstornoCompraApi(AuthenticatedView): 
    def post(self, request):
        data  = JSONParser().parse(request)
        status_code = data['authorization']['code']
        if status_code == "00":
            #TO DO - begin transaction

            # atualizar saldo
            conta = Conta.objects.get(account_id_paysmart=data['account_id'])

            conta_corrente = ContaCorrente.objects.get(conta=conta)
            amount_transaction = (float(data['chargeback_amount']['amount']) / 100)
            conta_corrente.saldo += amount_transaction
            conta_corrente.save()

            transacao = Transacao()
            transacao.authorization_id = uuid.uuid4().hex[:6].upper()
            transacao.obs = "Transacao de cancelamento realizada pela PAYSmart"
            transacao.conta = conta_corrente
            transacao.save()

            # TO DO - end transaction 

            # retornar a confirmacao
            return JsonResponse(data={
                "message": "Operação realizada com sucesso.",
                "code": 0,
                "authorization_id": transacao.pk,
                "balance": {
                    "amount": int(conta_corrente.saldo * 100),
                    "currency_code": 986
                }
            }, safe=False) 
                
            
        return JsonResponse(data=None, safe=False, status=499)
        

class SaldoApi(AuthenticatedView): 
    def post(self, request):
        data  = JSONParser().parse(request)
        status_code = data['authorization']['code']
        if status_code == "00":
            #TO DO - begin transaction

            # atualizar saldo
            conta = Conta.objects.get(account_id_paysmart=data['account_id'])
            conta_corrente = ContaCorrente.objects.get(conta=conta)

            transacao = Transacao()
            transacao.authorization_id = uuid.uuid4().hex[:6].upper()
            transacao.obs = "Consulta de saldo pela PAYSmart"
            transacao.conta = conta_corrente
            transacao.save()

            # TO DO - end transaction 

            # retornar a confirmacao
            return JsonResponse(data={
                "message": "Operação realizada com sucesso.",
                "code": 0,
                "authorization_id": transacao.pk,
                "balance": {
                    "amount": int(conta_corrente.saldo * 100),
                    "currency_code": 986
                }
            }, safe=False) 
                
            
        return JsonResponse(data=None, safe=False, status=499)
        
        