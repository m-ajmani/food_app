from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
	name = models.CharField(max_length=100)
	cost = models.IntegerField(1000, default=100)
	#inbag = models.ForeignKey

	def __str__(self):
		return self.name

class review(models.Model):
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
