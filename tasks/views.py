from django.shortcuts import render
from rest_framework import viewsets
from .models import Status, Task
from .serializers import StatusSerializer, TaskSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
