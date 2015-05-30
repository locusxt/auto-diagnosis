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
	response_data['questions'].append({'question' : '咳嗽持续天数', 'options' : ['一两天', '一两周', '大于两周']})
	response_data['questions'].append({'question' : '平均体温', 'options' : ['36-37摄氏度', '38摄氏度', '39摄氏度以上']})
	response_data['questions'].append({'question' : '头晕的程度', 'options' : ['可以忍受，不影响日程生活', '找不着北', '不能下床']})
	#response_data = {'questions' : 'haha'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def get_res(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	response_data = {'diseases' : [{'name':'感冒', 'prob':0.9}, {'name':'支气管炎', 'prob':0.5}, {'name':'肺炎', 'prob':0.3}]}
	return HttpResponse(json.dumps(response_data), content_type="application/json")