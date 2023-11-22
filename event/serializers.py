from rest_framework import serializers
from .models import Event, Type_Event


class Type_EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type_Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = '__all__'
