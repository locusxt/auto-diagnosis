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

@csrf_exempt
def get_modules(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	response_data = {'questions' : []}
	for i in range(20):
		response_data['questions'].append({'question' : 'hello?', 'options' : ['a', 'b', 'c']})
	#response_data = {'questions' : 'haha'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")