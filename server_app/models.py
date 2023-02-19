from django.contrib.auth.models import User, AbstractUser
from django.db import models

CURRENCY = (
    ("USD", "dollar"),
    ("BTC", "bitcoin"),
    ("ETH", "ethereum"),
    ("ADA", "cardano"),
    ("BNB", "binance_coin"),
    ("XRP", "xrp"),
    ("DOGE", "dogecoin"),
)

TIERS = (
    ("U", "User"),
    ("B", "Bronze"),
    ("S", "Silver"),
    ("G", "Gold"),
    ("A", "Admin"),

)


class Clan(models.Model):
    title = models.TextField(verbose_name="Название", max_length=20)
    clan_overall_balance = models.FloatField(verbose_name="Общий баланс клана", default=0)

    def __str__(self):
        return self.title


class Users(models.Model):
    name = models.TextField(verbose_name="Никнэйм", max_length=20)
    password = models.TextField(verbose_name="Пароль", max_length=100)
    phone_number = models.TextField(verbose_name="Номер телефона")
    tg_id = models.CharField(verbose_name="Телеграмм айди", max_length=100)
    data = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    tier = models.CharField(verbose_name='Статус', max_length=1, choices=TIERS, default="U")
    clan = models.ForeignKey(Clan, verbose_name='Клан', on_delete=models.CASCADE, null=True, blank=True, related_name='user')

    def __str__(self):
        return str(self.name)


class Wallet(models.Model):
    currency = models.CharField(verbose_name='Валюта', max_length=4, choices=CURRENCY, null=True, blank=True)
    users = models.ForeignKey(Users, verbose_name="Владелец кошелька", on_delete=models.CASCADE, related_name='wallets')
    amount = models.FloatField(verbose_name="Баланс", max_length=30)
    wallet_number = models.TextField(verbose_name='Id кошелька', default='111111')

    def __str__(self):
        return f"{str(self.users)} | {str(self.currency)}"


class Order(models.Model):
    user = models.ForeignKey(Users, verbose_name="Продавец", on_delete=models.CASCADE, related_name='user', default=1)
    currency = models.CharField(verbose_name='Валюта', max_length=4, choices=CURRENCY, null=True, blank=True)
    price = models.FloatField(verbose_name='Цена', max_length=100)
    amount = models.FloatField(verbose_name="Количество", max_length=100)
    date = models.DateTimeField(verbose_name="Дата выкладывания объявления", auto_now_add=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="application")


class PromoCodes(models.Model):
    code = models.TextField(verbose_name='Промокод', max_length=20)
    currency = models.CharField(verbose_name='Валюта', max_length=4, choices=CURRENCY, null=True, blank=True)
    amount = models.TextField(verbose_name='Количество', max_length=20)



class Transactions(models.Model):
    date = models.DateTimeField(verbose_name='Дата оплаты', auto_now_add=True)
    sender = models.TextField(verbose_name='Отправитель')
    sender_currency = models.CharField(max_length=4, choices=CURRENCY, null=True, blank=True)
    send_amount = models.FloatField(verbose_name='Отпраленно средств', max_length=100, default=0)
    recipient = models.TextField(verbose_name='Получатель')
    recipient_currency = models.CharField(max_length=4, choices=CURRENCY, null=True, blank=True)
    received_amount = models.FloatField(verbose_name='Полученно стредств', max_length=100, default=0)
    commission = models.FloatField(verbose_name="Комисиия", max_length=100, default=0)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactions")

    def __str__(self):
        return f"{self.sender} | {self.recipient} | {self.sender_currency} | {self.recipient_currency}"