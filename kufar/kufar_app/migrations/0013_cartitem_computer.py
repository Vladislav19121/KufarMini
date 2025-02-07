# Generated by Django 5.1.5 on 2025-02-07 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kufar_app', '0012_cartitem_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='computer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='kufar_app.computer'),
        ),
    ]
