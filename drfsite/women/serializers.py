from asyncore import read
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women
import io



# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content



class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = WomenModel('bogdan', 'some porfolio')
#     moder_sr = WomenSerializer(model)
#     print(moder_sr.data, type(moder_sr.data), sep='\n')
#     json = JSONRenderer().render(moder_sr.data)
#     print(json)


# def decrypt():
#     stream = io.BytesIO(b'{"title":"bogdan", "content":"some porfolio"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data) 