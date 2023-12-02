from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import TokenAuthentication

from .models import Event, Type_Event
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, Type_EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Type_EventViewSet(viewsets.ModelViewSet):
    queryset = Type_Event.objects.all()
    serializer_class = Type_EventSerializer


class EventAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class EventAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class EventAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsOwnerOrReadOnly,)
