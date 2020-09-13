from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import VideoSerializer
from .models import Video

import json
import operator

class ListQuizzes(APIView):
    def post(self, request, format=None):
        jsonRequest = json.loads(request.body.decode('utf-8'))

        print(jsonRequest['link'])

        return Response({'Link': jsonRequest['link'], 'Quiz': 'Dummy Data'})

# f="video_transcript_1.txt"
# f=open(f, 'r')

# #f="california is a city. india is a country. i love apples. the sun is big."

# list= [] #word list

# l=f.split()
# for w in l:
#       list.append(w)

# list.sort()

# dict= {}

# for w in list:
#     dict[w]=list.count(w)

# sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

# i=0
# while i<5:
#     print(sort_dict[i])
#     i+=1
    
# print("")
