from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        list_date = Women.objects.all().values()
        return Response({'posts':list(list_date)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post':model_to_dict(post_new)})

#class WomenAPIView(generics.ListAPIView):
 #   queryset = Women.objects.all()
 #  serializer_class = WomenSerializer

