from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone

# Create your models here.
EMPTY = 'EM'
CONSTANT = 'CO'
ACQUISITION = 'AC'
PROVIDERS = 'PR'
TYPE_CHOICES = [
    (EMPTY, 'בחר אפשררות'),
    (CONSTANT, 'קבועות'),
    (ACQUISITION, 'רכש'),
    (PROVIDERS, 'ספקים'),
]

YES = 'YE'
NO = 'NO'

IS_APPROVE_CHOICES = [
    (YES, 'כן'),
    (NO, 'לא'),
]


NOT_PAID = 'NP'
BACK_TRANSFER = 'BT'
DIRECT = 'DR'
CREDIT_CARD = 'CC'
CHECK = 'CH'
CACHE = 'CA'
PAID_CHOICES = [
    (NOT_PAID, 'לא שולם'),
    (BACK_TRANSFER, 'העברה בנקאית - ירוק'),
    (DIRECT, 'דיירקט עידן - צהוב'),
    (CREDIT_CARD, 'אשראי אופיר - כתום'),
    (CHECK, 'צ\'ק נייר - אדום'),
    (CACHE,'מזומן - כחול'),
]
IN_PC = 'PC'
PHYSICAL = 'PH'
DELIVERY = 'DL'
EMPTY = 'EM'

INVOICE_CHOICES = [
    
    (IN_PC, 'מסמך בתקייה במחשב - ירוק'),
    (PHYSICAL, 'קובץ נייר במגירה - צהוב'),
    (DELIVERY, 'במשלוח פיזי למשרד - כתום'),
    (EMPTY, 'אין חשבונית - אדום'),
]

class GeneralOrders(models.Model):

    created     = models.DateTimeField(editable=False)
    name        = models.CharField(max_length=250)
    providerName= models.CharField(max_length=100)
    total       = models.FloatField(null=True, blank=True)
    type        = models.CharField(max_length=2,choices=TYPE_CHOICES,default=EMPTY,)
    isApprove   = models.CharField(max_length=2,choices=IS_APPROVE_CHOICES,default=NO,)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()


        if self.isApprove == YES:
            print('is approve is true')
            obj = ApprovedOrders.objects.create(created=self.created,name=self.name, providerName=self.providerName, total=self.total, type=self.type, isApprove=self.isApprove)
            print(obj)
            #data, created = ApprovedOrders.objects.get_or_create(parent=self,)


        return super(GeneralOrders, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + '(' + str(self.total) + '₪)'


class ApprovedOrders(models.Model):


    #parent = models.ForeignKey(to=GeneralOrders, on_delete=models.CASCADE) #models.OneToOneField(to=GeneralOrders, on_delete=models.CASCADE)
    created     = models.DateTimeField(editable=False, null=True,)
    modified    = models.DateTimeField(auto_now=True)
    name        = models.CharField(max_length=250)
    providerName= models.CharField(max_length=100)
    total       = models.FloatField(null=True, blank=True)
    type        = models.CharField(max_length=2,choices=TYPE_CHOICES,default=EMPTY,)
    isApprove   = models.CharField(max_length=2,choices=[(YES, 'כן'),],default=YES,)
    invoiceNumber = models.CharField(max_length=50, blank=True)
    paidHow = models.CharField(max_length=2, choices=PAID_CHOICES,default=NOT_PAID)
    whenToPay = models.DateField(blank=True, null=True)
    invoiceLocation = models.CharField(max_length=2, choices=INVOICE_CHOICES, default=EMPTY)
