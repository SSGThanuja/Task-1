# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member, Audio, Photo, Household, Farm, Cropping, Point
from .serializers import MemberSerializer, HouseholdSerializer, AudioSerializer, PhotoSerializer, FarmSerializer, PointSerializer, CroppingSerializer

class HouseholdList(APIView):

	def get(self, response):

		hold = Household.objects.all()
		serializer11 = HouseholdSerializer(hold, many=True)
		return Response(serializer11.data)


class MemberList(APIView):

	def get(self, response):

		members = Member.objects.all()
		serializer = MemberSerializer(members, many = True)
		return Response(serializer.data)


class AudioList(APIView):

	def get(self, response):

		audios = Audio.objects.all()
		serializer1 = AudioSerializer(audios, many=True)
		return Response(serializer1.data)

class PhotoList(APIView):

	def get(self, response):

		photos = Photo.objects.all()
		serializer2 = PhotoSerializer(photos, many=True)
		return Response(serializer2.data)

class FarmList(APIView):

	def get(self, response):

		farms = Farm.objects.all()
		serializer3 = FarmSerializer(farms, many=True)
		return Response(serializer3.data)

class PointList(APIView):

	def get(self, response):

		points = Point.objects.all()
		serializer4 = PointSerializer(points, many=True)
		return Response(serializer4.data)

class CroppingList(APIView):

	def get(self, response):

		crops = Cropping.objects.all()
		serializer5 =CroppingSerializer(crops, many=True)
		return Response(serializer5.data)

