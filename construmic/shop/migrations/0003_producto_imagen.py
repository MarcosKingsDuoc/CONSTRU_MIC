# Generated by Django 5.0.4 on 2024-05-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_pedido_pedidoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]