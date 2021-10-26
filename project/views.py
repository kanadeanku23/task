from oauth2_provider.contrib.rest_framework import permissions, TokenHasReadWriteScope
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
