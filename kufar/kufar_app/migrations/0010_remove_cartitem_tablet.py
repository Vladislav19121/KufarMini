# Generated by Django 5.1.5 on 2025-02-06 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kufar_app', '0009_cartitem_tablet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='tablet',
        ),
    ]
