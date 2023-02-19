from rest_framework import serializers
from server_app.models import Users, Clan, PromoCodes, Wallet, Transactions, Order


class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = "__all__"


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PromoCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCodes
        fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"


class WalletTransactionsSerializer(serializers.ModelSerializer):
    wallet = TransactionsSerializer(many=True, read_only=True, source='transactions')

    class Meta:
        model = Wallet
        fields = ['users', 'amount', 'currency']


class ClanUsersSerializer(serializers.ModelSerializer):
    users = UsersSerializer(many=True, read_only=True, source='user')

    class Meta:
        model = Clan
        fields = ['title', 'clan_overall_balance', 'users']


class UsersWalletsSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer(read_only=True, many=True, source='wallets')

    class Meta:
        model = Users
        fields = ['name', 'phone_number', 'password', 'tg_id', 'tier', 'data', 'clan', 'wallet'] # 'name', 'overall_balance', 'balance', 'phone_number', 'tg_id', 'tier',


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"