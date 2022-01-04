from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .serializers import GameSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsOwnerOrReadOnly,)