# Generated by Django 4.0.5 on 2022-06-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('grupo', models.CharField(max_length=40)),
                ('planta', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
