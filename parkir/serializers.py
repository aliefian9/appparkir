# posts/serializers.py
from rest_framework import serializers
from . import models


class ParkirSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'Title', 'Status',)
        model = models.Parkir