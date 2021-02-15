from django.contrib import admin
from accounts.models import Profile,Therapist,CustomUser
from Ask_the_doctor.models import question_to_therapist,answers_from_therapist
from community_forum.models import Categories,Questions,Answers
#from therapist_dashboard.models import Patients
from private_chats.models import PersonalMessages,GroupMessages,Group
#Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Therapist)
admin.site.register(question_to_therapist)
admin.site.register(answers_from_therapist)
admin.site.register(Categories)
admin.site.register(Questions)
admin.site.register(Answers)
#admin.site.register(Comments)
#admin.site.register(Patients)
admin.site.register(PersonalMessages)
admin.site.register(Group)
admin.site.register(GroupMessages)

'''
admin.site.register(PersonalChatroom)

admin.site.register(FriendList)
admin.site.register(FriendRequest)
'''