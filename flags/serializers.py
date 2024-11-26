from rest_framework import serializers
from .models import Flags

class FlagsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flags
        fields = ['id', 'image', 'country_name']


class FlagsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flags
        fields = ['image', 'country_name']