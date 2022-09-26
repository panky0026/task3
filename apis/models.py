import genericpath
from django.db import models

# Create your models here.
class studentModel(models.Model):
	name = models.CharField(max_length = 200)
	classes = models.CharField(max_length = 200 , null=True)
	father_information = models.CharField(max_length = 200 , null=True)
	gender= (
        ('1','male'),     
        ('2', 'female'),
        ('3','transgender'),
    )
	gender = models.CharField(max_length=50,default="gender_type",choices=gender)




