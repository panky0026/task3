from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import studentSerializer
from .models import   studentModel



class studentViewSet(viewsets.ModelViewSet):
	# define queryset	
	queryset = studentModel.objects.all()
	
	# specify serializer to be used
	serializer_class = studentSerializer


