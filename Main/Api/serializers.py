from rest_framework import serializers
from .models import *

class FreeTrailerSerlizers(serializers.ModelSerializer):
    class Meta:
        model=FreeTriler
        fields = '__all__'