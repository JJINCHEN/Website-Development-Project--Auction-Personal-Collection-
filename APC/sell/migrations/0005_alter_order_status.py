# Generated by Django 3.2.8 on 2022-03-14 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_auto_20220228_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('0', 'Auction closed, unpaid'), ('1', 'Paid'), ('2', 'Undelivered'), ('3', 'Delivered'), ('4', 'Complete')], default='0', max_length=2, verbose_name='Status'),
        ),
    ]