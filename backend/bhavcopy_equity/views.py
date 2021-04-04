import os, json, csv, redis
import pandas as pd 
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .constants import Constants

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, 
                                    password=settings.REDIS_PASSWORD, charset="utf-8", decode_responses=True, db=0)


@api_view(['GET'])
def index(request):
    keys = redis_instance.keys(pattern=Constants.KEY_PATTERN.format(Constants.ASTERISK, Constants.ASTERISK))
    result = []
    for key in keys:
        result.append(redis_instance.hgetall(key))
    json_stuff = json.dumps(result)    
    return HttpResponse(json_stuff, content_type="text/json")

@api_view(['POST'])
@csrf_exempt
def download(request):
    df = pd.read_json(request.body.decode('utf-8'))
    data = (df).to_csv(index = False)
    return HttpResponse(data, content_type="text/csv")

@api_view(['POST'])
def do_search(request, *args, **kwargs):
    searchKey = request.body.decode('utf-8').upper() + Constants.ASTERISK
    redisKeys = redis_instance.keys(pattern=Constants.KEY_PATTERN.format(Constants.ASTERISK, searchKey))
    searchResult = []
    for key in redisKeys:
        searchResult.append(redis_instance.hgetall(key))
     
    return Response(searchResult, status=201)