
from rest_framework import serializers
from .models import GeneralOrders

class GeneralOrdersApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOrders
        fields = ('id','created','name','providerName','total','type','isApprove')
