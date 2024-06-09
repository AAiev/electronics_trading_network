from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from trading_platform.models import TradingLink, Product
from trading_platform.permissions import IsActiveUser
from trading_platform.serializers import TradingLinkSerializer, TradingLinkUpdateSerializer, ProductSerializer


class TradingLinkCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания объекта сети """
    serializer_class = TradingLinkSerializer
    permission_classes = [IsActiveUser]


class TradingLinkListAPIView(generics.ListAPIView):
    """ Контроллер просмотра списка объектов сети """
    queryset = TradingLink.objects.all()
    serializer_class = TradingLinkSerializer
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class TradingLinkRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра сущности объекта сети """
    queryset = TradingLink.objects.all()
    serializer_class = TradingLinkSerializer
    permission_classes = [IsActiveUser]


class TradingLinkUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер изменения объекта сети """
    queryset = TradingLink.objects.all()
    serializer_class = TradingLinkUpdateSerializer
    permission_classes = [IsActiveUser]


class TradingLinkDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер для удаления объекта сети """
    queryset = TradingLink.objects.all()
    permission_classes = [IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления моделью Продукты """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
