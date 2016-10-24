from rest_framework import serializers
from .models import Brand,CarModel,CarDetails

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name','cname')
		
class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('brand','model_name','cmodel_name')

class CarDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarDetails
		fields = ('carmodel_name','type','dengine','dpower','dtorque','dtransmission','pengine','ppower','ptorque','ptransmission','text')
		