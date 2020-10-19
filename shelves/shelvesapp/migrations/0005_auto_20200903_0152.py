# Generated by Django 3.1 on 2020-09-03 08:52

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shelvesapp', '0004_auto_20200903_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='', force_format='JPEG', keep_meta=True, quality=75, size=[500, 300], upload_to='images'),
        ),
    ]
