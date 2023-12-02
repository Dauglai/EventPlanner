from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Assume that you have installed requests: pip install requests
import requests
import json

from purchases.models import Purchase


class GenerateCredential(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        results = self.request.query_params.get('type')
        response = {}
        r = requests.get('https://randomuser.me/api/?results=40', auth=('user', 'pass'))
        r_status = r.status_code
        if r_status == 200:
            data = json.loads(r.json)
            for c in data:
                credential = Purchase(user=self.request.user, value=c)
                credential.save()
            response['status'] = 200
            response['message'] = 'success'
            response['credentials'] = data
        else:
            response['status'] = r.status_code
            response['message'] = 'error'
            response['credentials'] = {}
        return Response(response)


class UserCredentials(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        current_user = self.request.user
        credentials = Purchase.objects.filter(user__id=current_user)
        return Response(credentials)