from django.contrib.auth.models import User
from .serializers import SignUpSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)
