from django.urls import path
from . import views
app_name="private_chats"
urlpatterns = [
	path('<str:username>/',views.chat_room,name="chatroom"),
	path('<str:username>/chat/',views.index,name="index"),
	path('<str:username>/new/',views.search_results,name="search_results"),
	
	path('<str:username>/chat/new/<str:room_name>/',views.room,name="room"),	
	path('<str:username>/create_group/',views.create_group,name="creategroup"),
	path('<str:username>/groupchat/<int:pk>/',views.GroupView,name="groupchat"),
	path('<int:pk>/chat/<int:pk_alt>/',views.PrivateChatView,name="private"),
	path('members/',views.MembersView,name="members"),
	path('group_details/<int:pk>/',views.group_details,name="groupdetails")
]
'''
from django.urls import path
from direct.views import Inbox, UserSearch, Directs, NewConversation, SendDirect
urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),
   	path('<str:username>/chatroom/<int:pk>/',views.personalChatroomView,name="personal_chatroom"),
'''