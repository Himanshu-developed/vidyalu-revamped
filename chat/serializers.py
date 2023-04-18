from rest_framework import serializers
from chat.models import  Message

class MessageSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('thread','sender','text','created_at')