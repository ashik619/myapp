from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Brand,CarModel,CarDetails
from rest_framework import generics
from .serializer import BrandSerializer,ModelsSerializer,CarDetailSerializer

#class RESTmodels(generics.RetrieveUpdateDestroyAPIView):
class RESTmodels(generics.ListAPIView):
	
	
	def get_queryset(self):
		queryset = CarModel.objects.all()
		brandname = self.request.query_params.get('brandname', None)
		#return CarModel.objects.filter(brand=brandname)
		if brandname is not None:
			queryset = queryset.filter(brand__cname=brandname)
		return queryset
	serializer_class = ModelsSerializer

class RESTBrandList(generics.ListCreateAPIView):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	
class RESTCardetail(generics.ListAPIView):
	
	
	def get_queryset(self):
		queryset = CarDetails.objects.all()
		carname = self.request.query_params.get('carname', None)
		#return CarModel.objects.filter(brand=brandname)
		if carname is not None:
			queryset = queryset.filter(carmodel_name__cmodel_name=carname)
		return queryset
	serializer_class = CarDetailSerializer
def post_list(request):
    return render(request, 'blog/post_list.html', {})