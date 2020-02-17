from rest_framework import viewsets, generics
from fe7.models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # lookup_field = "name__iexact"

# class RetrieveCharacterView(generics.RetrieveAPIView):
#     lookup_field = "name"
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer
