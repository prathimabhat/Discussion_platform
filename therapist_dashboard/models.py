from django.db import models
from accounts.models import Profile,Therapist
# Create your models here.
'''class Patients(models.Model):
	class Meta:
		verbose_name_plural='Patients'

	MALE='MA'
	FEMALE='FE'
	OTHERS='OT'
	NOTDISCLOSE='NO'
	gender_choices=[
		(MALE,'Male'),
		(FEMALE,'Female'),
		(OTHERS,'Others'),
		(NOTDISCLOSE,'I do not wish to disclose')

	]
	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="patients",blank=True,null=True)
	therapist=models.ManyToManyField(Therapist,related_name="patients",blank=True)
	name=models.CharField(max_length=300,blank=True)
	gender=models.CharField(max_length=2,choices=gender_choices,default='NOTDISCLOSE')
	date_of_birth=models.DateField(blank=True,null=True)
	address=models.TextField(max_length=1000,blank=True)
	mental_illness=models.CharField(max_length=400,default='Not diagnosed yet')

	def __str__(self):
		return f"{self.id} -{self.name}"
'''
