# posts/serializers.py
from rest_framework import serializers
from . import models


class ParkirSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('Title', 'Status',)
        model = models.Parkir


class JumlahSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('Tersedia',)
        model = models.Jumlah
