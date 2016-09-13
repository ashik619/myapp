from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
	#b_id = models.IntegerField(primary_key = True, )
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
    
	
class CarModel(models.Model):
	brand = models.ForeignKey(Brand)
	model_name = models.CharField(max_length=100, default='nil')
	type = models.CharField(max_length=100, default='nil')
	dengine = models.CharField(max_length=200, default='nil')
	dpower = models.CharField(max_length=200, default='nil')
	dtorque = models.CharField(max_length=200, default='nil')
	dtransmission = models.CharField(max_length=200, default='nil')
	pengine = models.CharField(max_length=200, default='nil')
	ppower = models.CharField(max_length=200, default='nil')
	ptorque = models.CharField(max_length=200, default='nil')
	ptransmission = models.CharField(max_length=200, default='nil')
	text = models.TextField(default='nil')
	
	def __unicode__(self):
		return self.model_name