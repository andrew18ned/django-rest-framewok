from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        return Response({'title':'andrew17'})

#class WomenAPIView(generics.ListAPIView):
 #   queryset = Women.objects.all()
 #  serializer_class = WomenSerializer

