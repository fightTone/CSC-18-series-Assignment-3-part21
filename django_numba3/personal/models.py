from __future__ import unicode_literals

from django.db import models

class Stories(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

class User(models.Model):
	username = models.CharField(max_length=12)
	password = models.CharField(max_length=140)

	def __str__(self):
		return self.username