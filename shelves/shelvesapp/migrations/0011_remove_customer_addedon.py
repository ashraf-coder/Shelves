# Generated by Django 3.1 on 2020-10-01 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelvesapp', '0010_customer_addedon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='addedOn',
        ),
    ]
