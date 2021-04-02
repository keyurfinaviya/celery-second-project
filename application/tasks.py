from celery.schedules import crontab
from django.utils import timezone
from .models import Food
from celery import shared_task


@shared_task
def delete_old_food():
	foods = Food.objects.all()

	for food in foods:

		if food.expiration_date < timezone.now():
			food.delete()

	return "Compeleted deleting food at {}".format(timezone.now())