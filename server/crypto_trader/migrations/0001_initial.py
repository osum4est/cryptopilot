# Generated by Django 2.2.2 on 2019-06-18 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.CharField(max_length=16, unique=True)),
                ('base_currency', models.CharField(max_length=16)),
                ('quote_currency', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='TradeSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trader', models.CharField(max_length=256)),
                ('start_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('start_time', models.DateTimeField()),
                ('end_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('simulation', models.BooleanField()),
                ('active', models.BooleanField()),
                ('creator', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=12)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('time', models.DateTimeField()),
                ('notes', models.CharField(max_length=1024)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.crypto_trader.Currency', to_field='currency_id')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.crypto_trader.TradeSession')),
            ],
        ),
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('granularity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('low', models.DecimalField(decimal_places=2, max_digits=12)),
                ('high', models.DecimalField(decimal_places=2, max_digits=12)),
                ('open', models.DecimalField(decimal_places=2, max_digits=12)),
                ('close', models.DecimalField(decimal_places=2, max_digits=12)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.crypto_trader.Currency', to_field='currency_id')),
            ],
        ),
    ]
