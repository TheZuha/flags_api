from .models import Flags
from .serializers import FlagsListSerializers, FlagsDetailSerializers
from rest_framework import generics

# Create your views here.
class FlagsList(generics.ListCreateAPIView):
    queryset = Flags.objects.all()
    serializer_class = FlagsListSerializers

class FlagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flags.objects.all()
    serializer_class = FlagsDetailSerializers