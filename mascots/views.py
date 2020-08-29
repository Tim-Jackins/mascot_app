from .models import Mascot
from .serializers import MascotSerializer
from rest_framework import generics


class MascotListCreate(generics.ListCreateAPIView):
  queryset = Mascot.objects.all()
  serializer_class = MascotSerializer
