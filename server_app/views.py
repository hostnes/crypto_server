from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from server_app.models import Users, Clan, PromoCodes, Wallet, Transactions, Order
from server_app.serializers import ClanSerializer, UsersSerializer, PromoCodesSerializer, WalletSerializer, \
    TransactionsSerializer, WalletTransactionsSerializer, ClanUsersSerializer, UsersWalletsSerializer, \
    OrderSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "Ok"}, status.HTTP_200_OK)


"""
БАЗА
"""

class ClanList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class PromoCodesList(generics.ListCreateAPIView):
    queryset = PromoCodes.objects.all()
    serializer_class = PromoCodesSerializer


class WalletList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionsList(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'recipient']


"""
НЕ БАЗА
"""


class WalletTransactionsList(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletTransactionsSerializer


class ClanUsersList(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanUsersSerializer


class UsersWalletsList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersWalletsSerializer


class UsersWalletsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersWalletsSerializer


class UsersListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number', 'password']


class GetPasswordListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['password', 'tg_id']


class NameListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class PhoneNumberListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number']


class TgIdListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tg_id']


class WalletIdListView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['users', 'currency', 'wallet_number']


class WalletsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactinsRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class FindTransaction(generics.ListAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender', 'recipient']


class OrderRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'currency', 'wallet']
    pagination_class = LimitOffsetPagination

