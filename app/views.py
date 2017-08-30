# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,reverse

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect,HttpResponse
from .models import Member, Audio, Photo, Household, Farm, Cropping, Point
from .serializers import MemberSerializer, HouseholdSerializer, AudioSerializer, PhotoSerializer, FarmSerializer, PointSerializer, CroppingSerializer
from rest_framework import generics
import urllib2
import json 
class HouseholdList(generics.ListCreateAPIView):

		queryset = Household.objects.all()
		#serializer11 = HouseholdSerializer(hold, many=True)
		serializer_class = HouseholdSerializer
		#return Response(serializer11.data)


class MemberList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Member.objects.all()
		#serializer_class = MemberSerializer(members, many = True)
		serializer_class=MemberSerializer
		#return Response(serializer.data)


class AudioList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Audio.objects.all()
		#serializer_class = AudioSerializer(audios, many=True)
		serializer_class=AudioSerializer
		#return Response(serializer1.data)

class PhotoList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Photo.objects.all()
		#serializer2 = PhotoSerializer(photos, many=True)
		serializer_class=PhotoSerializer
		#return Response(serializer2.data)

class FarmList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Farm.objects.all()
		#serializer3 = FarmSerializer(farms, many=True)
		serializer_class=FarmSerializer
		#return Response(serializer3.data)

class PointList(generics.ListCreateAPIView):
	#def get(self, response):

		queryset = Point.objects.all()
		#serializer4 = PointSerializer(points, many=True)
		serializer_class=PointSerializer
		#return Response(serializer4.data)

class CroppingList(generics.ListCreateAPIView):

	#def get(self, response):

		queryset = Cropping.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=CroppingSerializer
		#return Response(serializer5.data)

class HouseholdDetail(generics.RetrieveUpdateDestroyAPIView):
		queryset = Household.objects.all()
		#serializer11 = HouseholdSerializer(hold, many=True)
		serializer_class=HouseholdSerializer
		#return Response(serializer11.data)

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Member.objects.all()
		#serializer_class = MemberSerializer(members, many = True)
		serializer_class=MemberSerializer
		#return Response(serializer.data)


class AudioDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Audio.objects.all()
		#serializer_class = AudioSerializer(audios, many=True)
		serializer_class=AudioSerializer
		#return Response(serializer1.data)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Photo.objects.all()
		#serializer2 = PhotoSerializer(photos, many=True)
		serializer_class=PhotoSerializer
		#return Response(serializer2.data)

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Farm.objects.all()
		#serializer3 = FarmSerializer(farms, many=True)
		serializer_class=FarmSerializer
		#return Response(serializer3.data)

class PointDetail(generics.RetrieveUpdateDestroyAPIView):
	#def get(self, response):

		queryset = Point.objects.all()
		#serializer4 = PointSerializer(points, many=True)
		serializer_class=PointSerializer
		#return Response(serializer4.data)

class CroppingDetail(generics.RetrieveUpdateDestroyAPIView):

	#def get(self, response):

		queryset = Cropping.objects.all()
		#serializer5 =CroppingSerializer(crops, many=True)
		serializer_class=CroppingSerializer
		#return Response(serializer5.data)


def read(request):
	
	req=urllib2.Request("http://127.0.0.1:8000/app/household/")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l=json.loads(f.read())
	k=[]
	name=request.POST['name']
	for i in l:
		if i['name']==name:
			k.append(i['name'])
			k.append(i['age'])
			k.append(i['gender'])
			contex={'k':k}
			return render(request,'app/show.html',contex)
		else:
			return HttpResponse("undone")





def index(request):
	return render(request,'app/index.html')


def create(request):
	name=request.POST['name']
	gender=request.POST['gender']
	age=request.POST['age']
	obj=Household(name=name,gender=gender,age=age)
	obj.save()
	return HttpResponseRedirect(reverse('app:index'))


