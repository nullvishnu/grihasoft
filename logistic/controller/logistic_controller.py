from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.shortcuts import render
import json
from logistic.data.request.logistics import LogisticsRequest
from logistic.service.logistic_service import Logistics_Service

def logistic_index(request):
    return render(request, 'index.html')

@csrf_exempt
@api_view(['GET','POST'])
def logistic_logic(request):
    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = Logistics_Service()
        data = LogisticsRequest(userdata)
        resp_obj = service.get_rate_logistics(data)
        return HttpResponse(resp_obj.get(), content_type='application/json')


@csrf_exempt
@api_view(['GET','POST'])
def logistics_fetch(request):
    if request.method == 'GET':
        service = Logistics_Service()
        resp_obj = service.get_logistics()
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = Logistics_Service()
        # data = UserRequest(userdata)
        emp_id = request.session['empid']
        data = {}
        resp_obj = service.insert_logistics(data,userdata,emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')

@csrf_exempt
@api_view(['GET','POST'])
def city_fetch(request):
    if request.method == 'GET':
        service = Logistics_Service()
        resp_obj = service.get_city()
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = Logistics_Service()
        # data = UserRequest(userdata)
        emp_id = request.session['empid']
        data = {}
        resp_obj = service.insert_city(data,userdata,emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')

@csrf_exempt
@api_view(['GET','POST'])
def zone_fetch(request):
    if request.method == 'GET':
        service = Logistics_Service()
        resp_obj = service.get_zone()
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = Logistics_Service()
        # data = UserRequest(userdata)
        emp_id = request.session['empid']
        data = {}
        resp_obj = service.insert_zone(data,userdata,emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')

@csrf_exempt
@api_view(['GET','POST'])
def rate_fetch(request):
    if request.method == 'GET':
        service = Logistics_Service()
        resp_obj = service.get_rate()
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = Logistics_Service()
        # data = UserRequest(userdata)
        emp_id = request.session['empid']
        data = {}
        resp_obj = service.insert_rate(data,userdata,emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')