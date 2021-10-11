from django.contrib import admin
from django.contrib.admin.sites import site
from django.db import models
from django import forms
from .models import ApprovedOrders, GeneralOrders

class GeneralOrdersForm(forms.ModelForm):
    
    class Meta:
        exclude = ['created',]
        model = GeneralOrders

# Register your models here.
class GeneralOrdersAdmin(admin.ModelAdmin):
    model = GeneralOrders
    list_display = ('created', 'name', 'providerName', 'total','type')
    list_editable = ('name', 'providerName', 'total', 'type')
    form = GeneralOrdersForm
admin.site.register(GeneralOrders, GeneralOrdersAdmin);


class ApprovedOrdersAdmin(admin.ModelAdmin):
    model = ApprovedOrders
    list_display = ('created','modified','name','providerName','total','type','invoiceNumber','paidHow','whenToPay','invoiceLocation')
    #readonly_fields= ('parent__name',)
    #list_editable  = ('parent_name',)

    #def parent_name(self, obj):
        #return obj.parent.name
admin.site.register(ApprovedOrders, ApprovedOrdersAdmin);
