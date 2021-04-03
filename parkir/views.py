from django.shortcuts import render
from rest_framework import generics

from .models import Parkir
from .serializers import ParkirSerializer

class ParkirList(generics.ListCreateAPIView):
    queryset = Parkir.objects.all()
    serializer_class = ParkirSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return ParkirSerializer

        return ParkirSerializer


class ParkirDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parkir.objects.all()
    serializer_class = ParkirSerializer