from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import VideoSerializer
from .models import Video

import json

class ListQuizzes(APIView):
    def get(self, request, format=None):
        jsonRequest = json.loads(request.body.decode('utf-8'))

        print(jsonRequest['link'])

        return Response({'Link': jsonRequest['link'], 'Quiz': 'Dummy Data'})