# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Household(models.Model):

	name = models.CharField(max_length = 200)
	gender_choices=(('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=1, choices = gender_choices)
	age = models.IntegerField()

	def __str__(self):

		return self.name


class Member(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	latitude = models.FloatField()
	longitude = models.FloatField()
	income = models.IntegerField()
	area = models.FloatField()

	def __float__(self):

		return self.latitude

class Photo(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	url = models.URLField()

	def __str__(self):
		return self.url

class Audio(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	clips = models.FilePathField()


class Farm(models.Model):

	H_id = models.ForeignKey(Household, on_delete = models.CASCADE)
	latitude = models.FloatField()
	longitude = models.FloatField()
	area = models.FloatField()

class Point(models.Model):

	F_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
	P_lat = models.FloatField()
	P_long = models.FloatField()


class Crop(models.Model):

	name = models.CharField(max_length = 50)


class Cropping(models.Model):

	F_id = models.ForeignKey(Farm, on_delete = models.CASCADE)
	crop_id = models.ForeignKey(Crop, on_delete= models.CASCADE)
	season_id = models.IntegerField()
	c_year = models.DateTimeField()
	c_area = models.FloatField()

