# Generated by Django 4.0.5 on 2022-06-21 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('fecha', models.CharField(max_length=40)),
                ('planta', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]