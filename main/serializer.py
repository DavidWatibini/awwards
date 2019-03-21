from rest_framework import serializers
from .models import *

class profile(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('name', 'description', 'price')
