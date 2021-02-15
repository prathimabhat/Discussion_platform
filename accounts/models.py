from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class CustomUser(AbstractUser):


	is_normal_user=models.BooleanField(default=True)

	objects=CustomUserManager() 

	def __str__(self):
		return f"{self.id}"

class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True)
    user_name=models.CharField(max_length=200,blank=True)
    first_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100,blank=True)
    email_id=models.EmailField(blank=True,null=True)
    reason = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joining=models.DateTimeField(auto_now_add=True)
    superuser=models.BooleanField(default=True)
    objects=CustomUserManager()
    

    def __str__(self):
    	return f"{self.user_name}"




class Therapist(models.Model):

   
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True)
    therapist_name=models.CharField(max_length=200,blank=True)
    therapist_email=models.EmailField(blank=True)
    office_address=models.TextField(max_length=800,blank=True)
    qualification=models.CharField(max_length=200,blank=True)
    specialization_area=models.CharField(max_length=400,blank=True)

    objects=CustomUserManager()

   

    def __str__(self):
        return f"{self.id}"




@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_normal_user:
            Profile.objects.create(user=instance)
        else:
            Therapist.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    try:
        if instance.is_normal_user:
            instance.profile.save()
        else:
            instance.therapist.save()
    except ObjectDoesNotExist:
        if instance.is_normal_user:
            Profile.objects.create(user=instance)
        else:
            Therapist.objects.create(user=instance)
