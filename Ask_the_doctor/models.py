from django.db import models
from accounts.models import Profile
from accounts.models import Therapist
from ckeditor.fields import RichTextField

# Create your models here.

class question_to_therapist(models.Model):
	class Meta:
		verbose_name_plural="Questions for therapists"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='questionfortherapist',blank=True,null=True)
	therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE,related_name='questionfortherapist',blank=True,null=True)
	question=RichTextField(blank=True,null=True)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id} "

	
class answers_from_therapist(models.Model):
	class Meta:
		verbose_name_plural="Answers from therapist"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='answersfromtherapist',blank=True,null=True)
	therapist=models.ForeignKey(Therapist,on_delete=models.CASCADE,related_name='answersfromtherapist',blank=True,null=True)
	question=models.ForeignKey(question_to_therapist,on_delete=models.CASCADE,related_name='answersfromtherapist',blank=True,null=True)
	answer=RichTextField(blank=True,null=True)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id} "
