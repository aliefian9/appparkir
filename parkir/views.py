from django.shortcuts import render
from rest_framework import generics

from .models import Parkir, Jumlah
from .serializers import ParkirSerializer, JumlahSerializer

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


class JumlahList(generics.ListCreateAPIView):
    queryset = Jumlah.objects.all()
    serializer_class = JumlahSerializer

class JumlahDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jumlah.objects.all()
    serializer_class = JumlahSerializer