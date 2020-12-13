from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import JsonResponse
from rest_framework import status
from transacao.models import *
from transacao.serializers import CompraSerializer

class AuthenticatedView(APIView):
    permission_classes = (
     IsAuthenticated,)


class NotAuthenticatedView(APIView):
    permission_classes = (
     AllowAny,)

class StatusApi(AuthenticatedView):    
    def get(self, request):
        return JsonResponse(data={
            'message' : 'Operação realizada com sucesso.',
            'code' : 0
        }, safe=False, status=status.HTTP_200_OK)
        