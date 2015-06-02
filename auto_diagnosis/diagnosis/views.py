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
	response_data = {'modules' : ['呼吸系统', '消化系统', '血液系统']}
	#response_data = {'questions' : 'haha'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def get_module_questions(request):
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

@csrf_exempt
def get_details(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	response_data = {'details' : '常见症状，发烧，流鼻涕，咳嗽；常用治疗手段，多读书，多看报，少玩游戏，多睡觉'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_disease_questions(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	response_data = {'adv_questions' : []}
	response_data['adv_questions'].append({'question' : '白细胞数量', 'options' : ['找不到', '100个', '200个', '很多个']})
	response_data['adv_questions'].append({'question' : '红细胞数量', 'options' : ['找不到', '100个', '200个', '很多个']})
	response_data['adv_questions'].append({'question' : '血小板数量', 'options' : ['找不到', '100个', '200个', '很多个']})
	#response_data = {'questions' : 'haha'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_treatment(request):
	if not request.is_ajax():
		return HttpResponse("Not Ajax")
	if request.method != 'POST':
		return HttpResponse("Not Ajax Post")
	d = json.loads(request.body)
	print(d)
	response_data = {'treatment' : '你需要一碗包治百病的板蓝根'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")
