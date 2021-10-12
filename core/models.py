from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone

# Create your models here.
EMPTY = 'ריק'
CONSTANT = 'קבועות'
ACQUISITION = 'רכש'
PROVIDERS = 'ספקים'
TYPE_CHOICES = [
    (EMPTY, 'בחר אפשררות'),
    (CONSTANT, 'קבועות'),
    (ACQUISITION, 'רכש'),
    (PROVIDERS, 'ספקים'),
]

YES = 'כן'
NO = 'לא'

IS_APPROVE_CHOICES = [
    (YES, 'כן'),
    (NO, 'לא'),
]


NOT_PAID = 'לא שולם'
BACK_TRANSFER = 'העברה בנקאית'
DIRECT = 'דיירקט עידן'
CREDIT_CARD = 'אשראי אופיר'
CHECK =  'צ\'ק נייר'
CACHE = 'מזומן'
PAID_CHOICES = [
    (NOT_PAID, 'לא שולם'),
    (BACK_TRANSFER, 'העברה בנקאית - ירוק'),
    (DIRECT, 'דיירקט עידן - צהוב'),
    (CREDIT_CARD, 'אשראי אופיר - כתום'),
    (CHECK, 'צ\'ק נייר - אדום'),
    (CACHE,'מזומן - כחול'),
]
IN_PC = 'מסמך בתקייה במחשב'
PHYSICAL = 'קובץ נייר במגירה'
DELIVERY = 'במשלוח פיזי למשרד'
NON_REPORTABLE = 'לא ניתן לדיווח'
EMPTY = 'אין חשבונית'

INVOICE_CHOICES = [
    
    (IN_PC, 'מסמך בתקייה במחשב - ירוק'),
    (PHYSICAL, 'קובץ נייר במגירה - צהוב'),
    (DELIVERY, 'במשלוח פיזי למשרד - כתום'),
    (NON_REPORTABLE, 'לא ניתן לדיווח'),
    (EMPTY, 'אין חשבונית - אדום'),
]

class GeneralOrders(models.Model):

    created     = models.DateTimeField(editable=False)
    name        = models.CharField(max_length=250)
    providerName= models.CharField(max_length=100)
    total       = models.FloatField(null=True, blank=True)
    type        = models.CharField(max_length=50,choices=TYPE_CHOICES,default=EMPTY,)
    #isApprove   = models.CharField(max_length=50,choices=IS_APPROVE_CHOICES,default=NO,)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
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
    type        = models.CharField(max_length=50,choices=TYPE_CHOICES,default=EMPTY,)
    #isApprove   = models.CharField(max_length=50,choices=[(YES, 'כן'),],default=YES,)
    invoiceNumber = models.CharField(max_length=50, blank=True)
    paid = models.BooleanField(default=False)
    paidHow = models.CharField(max_length=50, choices=PAID_CHOICES,default=NOT_PAID)
    whenToPay = models.DateField(blank=True, null=True)
    invoiceLocation = models.CharField(max_length=50, choices=INVOICE_CHOICES, default=EMPTY)



class ArchivedOrders(models.Model):
    #parent = models.ForeignKey(to=GeneralOrders, on_delete=models.CASCADE) #models.OneToOneField(to=GeneralOrders, on_delete=models.CASCADE)
    created     = models.DateTimeField(editable=False, null=True,)
    modified    = models.DateTimeField(auto_now=True)
    name        = models.CharField(max_length=250)
    providerName= models.CharField(max_length=100)
    total       = models.FloatField(null=True, blank=True)
    type        = models.CharField(max_length=50,choices=TYPE_CHOICES,default=EMPTY,)
    invoiceNumber = models.CharField(max_length=50, blank=True)
    paid = models.BooleanField(default=False)
    paidHow = models.CharField(max_length=50, choices=PAID_CHOICES,default=NOT_PAID)
    whenToPay = models.DateField(blank=True, null=True)
    invoiceLocation = models.CharField(max_length=50, choices=INVOICE_CHOICES, default=EMPTY)