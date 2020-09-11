from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

import json
from .models import SeaData
import logging

logger = logging.getLogger('django.request')

# Create your views here.

def csrf_token(request):
    response = {}
    response['error'] = ''

    try:
        token = get_token(request)
        response['token'] = token
    except Exception as e:
        logger.debug(e)
        response['error'] = str(e)

    return JsonResponse(response)

@csrf_exempt
def list(request):
    logger.debug(request)
    response = {}
    response['error'] = ''
    try:
        seadata = SeaData.objects.filter()[:20]
        response['items']  = json.loads(serializers.serialize("json", seadata))
    except Exception as e:
        logger.error(e);
        response['error'] = str(e)

    return JsonResponse(response)
