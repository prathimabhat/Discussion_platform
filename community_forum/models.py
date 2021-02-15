from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import Profile
# Create your models here.
class Categories(models.Model):
	class Meta:
		verbose_name_plural="Categories"

	id=models.AutoField(primary_key=True,unique=True)
	category_name=models.CharField(max_length=200,blank=True)

	def __str__(self):
		return f"{self.category_name}"


class Questions(models.Model):
	class Meta:
		verbose_name_plural="Questions"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='questions',blank=True,null=True)
	category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='questions',blank=True,null=True)
	question_title=models.CharField(max_length=300,blank=True,null=True)
	question_detail=RichTextField(blank=True,null=True)
	up_votes=models.ManyToManyField(Profile,related_name='questions_up_votes')
	down_votes=models.ManyToManyField(Profile,related_name='questions_down_votes')
	date=models.DateTimeField(auto_now_add=True)
	anonymous=models.BooleanField(default=False)

	def __str__(self):
		return f"{self.question_title}"

	def total_upvotes(self):
		return self.up_votes.count()
	def total_downvotes(self):
		return self.down_votes.count()

'''class QuestionVotes(models.Model):
	class Meta:
		verbose_name_plural= "Question Votes"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='questionvotes',blank=True,null=True)
	question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='questionvotes',blank=True,null=True)
	up_votes=models.IntegerField(blank=True)
	down_votes=models.IntegerField(blank=True)

	def __str__(self):
		return f"{self.id}"
'''

class Answers(models.Model):
	class Meta:
		verbose_name_plural="Answers"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='answers',blank=True,null=True)
	category=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='answers',blank=True,null=True)
	question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='answers',blank=True,null=True)
	answer=RichTextField(blank=True,null=True)
	up_votes=models.ManyToManyField(Profile,related_name='answers_up_votes')
	down_votes=models.ManyToManyField(Profile,related_name='answers_down_votes')
	date=models.DateTimeField(auto_now_add=True)
	anonymous = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.id}"

	def total_upvotes(self):
		return self.up_votes.count()
	def total_downvotes(self):
		return self.down_votes.count()


'''class AnswerVotes(models.Model):
	class Meta:
		verbose_name_plural="Answer Votes"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='answervotes',blank=True,null=True)
	answer=models.ForeignKey(Answers,on_delete=models.CASCADE,related_name='answervotes',blank=True,null=True)
	up_votes=models.IntegerField(blank=True)
	down_votes=models.IntegerField(blank=True)

	def __str__(self):
		return f"{self.id}"
'''

'''class Comments(models.Model):
	class Meta:
		verbose_name_plural="Comments"

	id=models.AutoField(primary_key=True,unique=True)
	user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='Comments',blank=True,null=True)
	question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Comments',blank=True,null=True)
	comment=RichTextField(blank=True,null=True)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id}"
'''


