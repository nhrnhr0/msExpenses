from django.contrib import admin
from django.contrib.admin.sites import site
from .models import ApprovedOrders, GeneralOrders
# Register your models here.
class GeneralOrdersAdmin(admin.ModelAdmin):
    model = GeneralOrders
    list_display = ('created', 'name', 'providerName', 'total','type',  'isApprove')
    list_editable = ('name', 'providerName', 'total', 'type', 'isApprove')
admin.site.register(GeneralOrders, GeneralOrdersAdmin);


class ApprovedOrdersAdmin(admin.ModelAdmin):
    model = ApprovedOrders
    #list_display = ['__all__',]
    #readonly_fields= ('parent__name',)
    #list_editable  = ('parent_name',)

    #def parent_name(self, obj):
        #return obj.parent.name
admin.site.register(ApprovedOrders, ApprovedOrdersAdmin);
