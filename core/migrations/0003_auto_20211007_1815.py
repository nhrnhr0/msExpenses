# Generated by Django 3.2.8 on 2021-10-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211007_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedorders',
            name='invoiceLocation',
            field=models.CharField(choices=[('PC', 'מסמך בתקייה במחשב - ירוק'), ('PH', 'קובץ נייר במגירה - צהוב'), ('DL', 'במשלוח פיזי למשרד - כתום'), ('EM', 'אין חשבונית - אדום')], default='EM', max_length=2),
        ),
        migrations.AlterField(
            model_name='approvedorders',
            name='whenToPay',
            field=models.DateField(blank=True),
        ),
    ]
