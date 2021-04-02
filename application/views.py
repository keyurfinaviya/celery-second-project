from django.shortcuts import render
import datetime
from django.utils import timezone
from .models import Food
from django.http import HttpResponse
# Create your views here.


def add_food(self):
	Food.objects.create(expiration_date=timezone.now() + datetime.timedelta(seconds=200))
	return HttpResponse("")

	