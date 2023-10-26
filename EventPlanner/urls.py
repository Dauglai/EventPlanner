"""
URL configuration for EventPlanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from event.views import EventViewSet, Type_EventViewSet
from tasks.views import TaskViewSet, StatusViewSet

router = routers.SimpleRouter()
router.register(r'event', EventViewSet)
router.register(r'type_event', Type_EventViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/event/
]