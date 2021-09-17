from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework import generics

from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import TokenSerializer, RegisterUserSerializer

# Create your views here.
class TokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

