# Generated by Django 4.1.3 on 2022-12-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0008_rename_amount_minus_transactions_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='recipient_currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('ADA', 'cardano'), ('BNB', 'binance_coin'), ('XRP', 'xrp'), ('DOGE', 'dogecoin')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='sender_currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('ADA', 'cardano'), ('BNB', 'binance_coin'), ('XRP', 'xrp'), ('DOGE', 'dogecoin')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollar'), ('BTC', 'bitcoin'), ('ETH', 'ethereum'), ('ADA', 'cardano'), ('BNB', 'binance_coin'), ('XRP', 'xrp'), ('DOGE', 'dogecoin')], max_length=4, null=True),
        ),
    ]