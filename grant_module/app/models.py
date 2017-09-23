from django.db import models
from django.contrib.auth.models import User

class Grant(models.Model):
	title = models.CharField(max_length=300)
	date= models.CharField(max_length=100)
	link = models.CharField(max_length=300,default="")

	def __str__(self):
		return self.title;

