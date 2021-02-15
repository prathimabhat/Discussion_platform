from django.db import models
from accounts.models import Profile
from django.conf import settings
from django.utils import timezone
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
'''
class Message(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user')
	sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='from_user')
	recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='to_user')
	body = models.TextField(max_length=1000, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def send_message(from_user, to_user, body):
		sender_message = Message(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			is_read=True)
		sender_message.save()

		recipient_message = Message(
			user=to_user,
			sender=from_user,
			body=body,
			recipient=from_user,)
		recipient_message.save()
		return sender_message

	def get_messages(user):
		messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': User.objects.get(pk=message['recipient']),
				'last': message['last'],
				'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users



'''



class PersonalMessages(models.Model):

	class Meta:
		verbose_name_plural="Personal messages"
	id=models.AutoField(primary_key=True,unique=True)
	msg_sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="msg_sender",blank=True,null=True)
	msg_receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="msg_receiver",blank=True,null=True)
	message=models.TextField(max_length=2000)
	msg_sent_time=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id}"


class Group(models.Model):
	id=models.AutoField(primary_key=True,unique=True)
	name=models.CharField(max_length=50)
	admin=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="grouproom",blank=True,null=True)
	members=models.ManyToManyField(Profile,related_name='group_members')
	def __str__(self):
		return f"{self.id}"

class GroupMessages(models.Model):
	class Meta:
		verbose_name_plural="Group messages"
	id=models.AutoField(primary_key=True,unique=True)
	grouproom=models.ForeignKey(Group,on_delete=models.CASCADE,related_name="group_message",blank=True,null=True)
	sender=models.ForeignKey(Profile,on_delete=models.DO_NOTHING,related_name="groupchatuser")
	msg_sent_time=models.DateTimeField(auto_now_add=True)
	content=models.TextField(max_length=2000)

	def __str__(self):

		return f"{self.id} {self.sender}"

	def last_10_messages(self):
		return GroupMessages.objects.order_by('-timestamp').all()[:10]



	
		