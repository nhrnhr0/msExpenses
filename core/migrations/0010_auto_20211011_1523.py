# Generated by Django 3.2.8 on 2021-10-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211011_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedorders',
            name='invoiceLocation',
            field=models.CharField(choices=[('מסמך בתקייה במחשב', 'מסמך בתקייה במחשב - ירוק'), ('קובץ נייר במגירה', 'קובץ נייר במגירה - צהוב'), ('במשלוח פיזי למשרד', 'במשלוח פיזי למשרד - כתום'), ('אין חשבונית', 'אין חשבונית - אדום')], default='אין חשבונית', max_length=50),
        ),
        migrations.AlterField(
            model_name='approvedorders',
            name='type',
            field=models.CharField(choices=[('ריק', 'בחר אפשררות'), ('קבועות', 'קבועות'), ('רכש', 'רכש'), ('ספקים', 'ספקים')], default='אין חשבונית', max_length=50),
        ),
        migrations.AlterField(
            model_name='generalorders',
            name='type',
            field=models.CharField(choices=[('ריק', 'בחר אפשררות'), ('קבועות', 'קבועות'), ('רכש', 'רכש'), ('ספקים', 'ספקים')], default='אין חשבונית', max_length=50),
        ),
    ]
