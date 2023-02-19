# Generated by Django 4.1.3 on 2023-01-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0016_rename_application_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocodes',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('ADA', 'cardano'), ('BNB', 'binance_coin'), ('XRP', 'xrp'), ('DOGE', 'dogecoin')], max_length=4, null=True, verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallet_id',
            field=models.TextField(default='111111', verbose_name='Id кошелька'),
        ),
        migrations.AlterField(
            model_name='promocodes',
            name='code',
            field=models.TextField(max_length=20, verbose_name='Промокод'),
        ),
    ]
