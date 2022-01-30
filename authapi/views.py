from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics

# Create your views here.
User = get_user_model()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer