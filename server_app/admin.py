from django.contrib import admin

from server_app.models import Users, Clan, PromoCodes, Wallet, Transactions, Order


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("title", "clan_overall_balance")


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", "tier", "phone_number")


@admin.register(PromoCodes)
class PromoCodesAdmin(admin.ModelAdmin):
    list_display = ("code", "amount")


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("users", "currency", "amount")


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "sender_currency", "recipient_currency")


@admin.register(Order)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('user', "currency", "price", "amount")


