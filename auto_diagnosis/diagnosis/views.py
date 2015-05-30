from django.shortcuts import render

from django.shortcuts import render_to_response
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def start_diagnosis(request):
    return render_to_response('diagnosis.html')
