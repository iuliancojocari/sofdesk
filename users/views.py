from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import SignupSerializer


class SignupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]
