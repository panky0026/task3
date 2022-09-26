# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import studentModel

# Create a model serializer


class studentSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = studentModel
		fields = ('name','gender','classes','father_information')

