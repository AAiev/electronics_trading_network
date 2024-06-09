from rest_framework.routers import DefaultRouter
from django.urls import path

from trading_platform.apps import TraidngPlatfomConfig
from trading_platform.views import *

app_name = TraidngPlatfomConfig.name

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('tl/create/', TradingLinkCreateAPIView.as_view(), name='tl_create'),
    path('tl/', TradingLinkListAPIView.as_view(), name='tl_list'),
    path('tl/<int:pk>/', TradingLinkRetrieveAPIView.as_view(), name='tl_get'),
    path('tl/update/<int:pk>/', TradingLinkUpdateAPIView.as_view(), name='tl_update'),
    path('tl/delete/<int:pk>/', TradingLinkDestroyAPIView.as_view(), name='tl_delete'),

] + router.urls
