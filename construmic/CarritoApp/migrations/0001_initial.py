# Generated by Django 5.0.1 on 2024-05-08 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=32)),
                ('alto', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('ancho', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField()),
                ('estado', models.IntegerField(choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Reacondicionado')])),
                ('imagen', models.BinaryField()),
            ],
        ),
    ]
