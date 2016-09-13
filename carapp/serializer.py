from rest_framework import serializers
from .models import Brand,CarModel

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)
		
class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('brand','model_name','type','dengine','dpower','dtorque','dtransmission',
					'pengine','ppower','ptorque','ptransmission','text')