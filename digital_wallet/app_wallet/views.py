from decimal import Decimal
from .serializer.serializer import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework import status, permissions
from .models import BalanceDetail, Transaction
from app_user.models import *
import random


class BalanceApiView(APIView):
    """
        Class where the method needs a id to return or update
        any information
    """

    def getObject(self, id):
        """
            Validated if object exist
        """
        valor = BalanceDetail.objects.filter(
            user_id=id).values('balance', 'user__name', 'user__identification_number').first()

        return (valor)

    def get(self, request, id):
        current_balance = self.getObject(id)
        serializer = BalanceSerializer(current_balance)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReloadMoneyView(APIView):
    """
        Class where the method needs a id to return or update any information
        ejemplo de json
        {
            "identification": "123456789",
            "reload": 100
        }

    """

    #permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        identification = request.data['identification']
        print("")
        try:
            id_user = User.objects.filter(
                identification_number=identification).values('id').first()['id']
        except:
            return Response({'mensaje': 'usuario no existe'}, status=status.HTTP_404_NOT_FOUND)

        # current_balance = BalanceDetail.objects.filter(
        #     user_id=id_user).values('balance').first()['balance']
      
        new_balance = BalanceDetail.objects.get(user_id=id_user)

        new_balance.balance = new_balance.balance + request.data['reload']
        print(new_balance.balance)
        try:
            new_balance.save()
            print(new_balance.balance)
        except Exception as e:
            print(f"Error al guardar el balance: {e}")

        return Response(status=status.HTTP_201_CREATED)


"""
  The `PayView` class is an API view that allows users to make transactions by deducting the  transaction amount from their current balance.
"""


# @method_decorator(csrf_exempt, name='dispatch')
class PayView(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (SessionAuthentication,)

    def post(self, request):

        # cambiar por  cedula la id
        id = request.data['user']
        current_balance = BalanceDetail.objects.filter(user_id=id).values('balance').first()
        current_balance = current_balance['balance']

        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            validatedData = serializer.validated_data

            transaction = Transaction(**validatedData)
            # transaction.amount
            if current_balance >= transaction.amount:
                transaction.save()
                new_balance = BalanceDetail.objects.get(
                    user_id=id)
                new_balance.balance = (current_balance - transaction.amount)
                new_balance.save()
                serializerResponse = TransactionSerializer(
                    transaction)
                return Response(serializerResponse.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"mensaje": "saldo insuficiente"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserWithdrawal(APIView):
    #permission_classes = (permissions.AllowAny,)
    #authentication_classes = (SessionAuthentication,)
    def post(self, request):
        """
        JSON de entrada:
        {
            "identification_number": "123456789",
            "value": 20000
        }
        """
        code = random.randint(100000, 999999)
        data2 = request.data
        data2["code_validation"] = str(code)
        identification_number = data2["identification_number"]

        try:
            withdrawal_m = withdrawal.objects.get(identification_number=identification_number)
            
            withdrawal_m.code_validation = data2["code_validation"]
            withdrawal_m.value = data2["value"]
            withdrawal_m.save()

            return Response({"code_validation": withdrawal_m.code_validation}, status=status.HTTP_200_OK)

        except withdrawal.DoesNotExist:

            serializer = withdrawalSerializer(data=data2)
            if serializer.is_valid(raise_exception=True):

                withdrawal_m = withdrawal(**data2)
                withdrawal_m.save()
                print(withdrawal_m)

                return Response({"mensaje": withdrawal_m.code_validation}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class CorresponsalWithdrawal(APIView):

    def post(self, request):
        """
        JSON de entrada:
        {
            "identification_number": "123456789",
            "code_validation": "20000"
        }
        """
        serializer = withdrawalBalanceDetailSerializer(data=request.data)
        
        if serializer.is_valid():
            identification_number = request.data['identification_number']
            id_user = User.objects.filter(identification_number=identification_number).values('id').first()
            
            if id_user:
                balanceDetail = BalanceDetail.objects.filter(user_id=id_user["id"]).first()
                withdrawal_m = withdrawal.objects.get(identification_number=identification_number)

                if balanceDetail.balance >= withdrawal_m.value:
                    balanceDetail.balance = (balanceDetail.balance - withdrawal_m.value)
                    balanceDetail.save()
                    withdrawal_m.delete()
                    return Response({"mensaje": "retiro exitoso", "id":id_user["id"],"amount":withdrawal_m.value}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"mensaje": "Saldo insuficiente"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"mensaje": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje": "Error de validación"}, status=status.HTTP_400_BAD_REQUEST)
