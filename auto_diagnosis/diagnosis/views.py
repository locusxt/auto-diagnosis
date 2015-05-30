# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def start_diagnosis(request):
    return render_to_response('diagnosis.html')

def get_states(request):
    response_data = {'states':['发烧', '头痛', '咳嗽', '头晕', '乏力', '背痛']}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
