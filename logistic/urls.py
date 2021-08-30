from django.contrib import admin
from django.urls import path
from logistic.controller import logistic_controller

urlpatterns = [
    path('', logistic_controller.logistic_index),
    path('logic', logistic_controller.logistic_logic),
    path('submit', logistic_controller.logistics_fetch),
    path('city', logistic_controller.city_fetch),
    path('rate', logistic_controller.rate_fetch),
    path('zone', logistic_controller.zone_fetch),
]