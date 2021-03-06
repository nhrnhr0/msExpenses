# Generated by Django 3.2.8 on 2021-10-07 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_approvedorders_whentopay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvedorders',
            name='paid',
        ),
        migrations.AlterField(
            model_name='approvedorders',
            name='paidHow',
            field=models.CharField(choices=[('NP', 'לא שולם'), ('BT', 'העברה בנקאית - ירוק'), ('DR', 'דיירקט עידן - צהוב'), ('CC', 'אשראי אופיר - כתום'), ('CH', "צ'ק נייר - אדום"), ('CA', 'מזומן - כחול')], default='NP', max_length=2),
        ),
        migrations.AlterField(
            model_name='approvedorders',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.generalorders'),
        ),
        migrations.AlterField(
            model_name='generalorders',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
