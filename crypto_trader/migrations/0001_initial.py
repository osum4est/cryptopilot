# Generated by Django 2.2.2 on 2019-06-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.CharField(max_length=16)),
                ('granularity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=2, max_digits=12)),
                ('high', models.DecimalField(decimal_places=2, max_digits=12)),
                ('open', models.DecimalField(decimal_places=2, max_digits=12)),
                ('close', models.DecimalField(decimal_places=2, max_digits=12)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.CharField(max_length=16, unique=True)),
                ('base_currency', models.CharField(max_length=16)),
                ('quote_currency', models.CharField(max_length=16)),
            ],
        ),
    ]
