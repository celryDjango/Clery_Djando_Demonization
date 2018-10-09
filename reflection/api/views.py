# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from api.models import *
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# import line for 
from .tasks import addition

@api_view(['GET', 'POST'])
def addition_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        a =addition.delay()
        print(a)
        return JsonResponse({"meaasge":str(a)})