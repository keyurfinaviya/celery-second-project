from django.db import models

# Create your models here.

class Food(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	expiration_date = models.DateTimeField()
