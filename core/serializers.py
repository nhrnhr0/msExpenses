
from rest_framework import serializers
from .models import ApprovedOrders, GeneralOrders

class GeneralOrdersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOrders
        fields = ('id','created','name','providerName','total','type')


class ApprovedOrdersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedOrders
        fields = ('id', 'created', 'name','providerName', 'total', 'type', 'invoiceNumber', 'paidHow', 'whenToPay', 'invoiceLocation')