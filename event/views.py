from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Type_Event
from .serializers import EventSerializer, Type_EventSerializer


class Type_EventViewSet(viewsets.ModelViewSet):
    queryset = Type_Event.objects.all()
    serializer_class = Type_EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
