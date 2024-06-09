from rest_framework import generics, permissions

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания сущности для модели Пользователя
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
