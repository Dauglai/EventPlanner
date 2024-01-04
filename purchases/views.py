from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
import requests
import json

from event.permissions import IsOwnerOrReadOnly
from purchases.models import Purchase, Link, TypePurchase
from purchases.serializers import PurchaseSerializer


class PurchaseAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        lst = Purchase.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        link = Link.objects.create(
            link=request.data['link']
        )
        response = requests.get(url=link.link)
        data = response.json()
        result = json.loads(data)
        post_new = Purchase.objects.create(

        )

class PurchaseAPIList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PurchaseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PurchaseAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = (IsOwnerOrReadOnly,)