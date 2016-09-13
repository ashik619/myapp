from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Brand,CarModel
from rest_framework import generics
from .serializer import BrandSerializer,ModelsSerializer

#class RESTmodels(generics.RetrieveUpdateDestroyAPIView):
class RESTmodels(generics.ListAPIView):
	
	
	def get_queryset(self):
		queryset = CarModel.objects.all()
		brandname = self.request.query_params.get('brandname', None)
		#return CarModel.objects.filter(brand=brandname)
		if brandname is not None:
			queryset = queryset.filter(brand__name=brandname)
		return queryset
	serializer_class = ModelsSerializer

class RESTBrandList(generics.ListCreateAPIView):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer