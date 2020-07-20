from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Todo':'To be created',
    }
    return Response(api_urls)
