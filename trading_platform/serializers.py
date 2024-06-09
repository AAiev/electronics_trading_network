from rest_framework import serializers

from trading_platform.models import Product, TradingLink


class TradingLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradingLink
        fields = '__all__'


class TradingLinkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradingLink
        exclude = ['arrear']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'release_date')
