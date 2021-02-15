from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile,CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .forms import TxtForm,GrpForm,NewGroupForm
from .models import PersonalMessages,GroupMessages,Group
from django.http import HttpResponse,Http404
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
# Create your views here.
@login_required
def index(request,*args,**kwargs):
	return render(request,'private_chats/index.html',{})
@login_required
def room(request,*args,**kwargs):
	room_name=kwargs['room_name']
	return render(request,'private_chats/chat_room.html',
		{
		'room_name':room_name
		})


@login_required
def chat_room(request,*args, **kwargs):
   
    user=get_object_or_404(Profile,user_name=kwargs['username'])
   
    contacts=PersonalMessages.objects.filter(msg_sender=request.user.profile.id)
    msgs_received=PersonalMessages.objects.filter(msg_receiver=request.user.profile.id)
    my_groups=Group.objects.filter(admin=request.user.profile.id)
    groups=Group.objects.filter(members=request.user.profile.id)
    context={
        'user':user,
        'contacts':contacts,
        'my_groups':my_groups,
        'groups':groups,
        'msgs_received':msgs_received
        
    }
    return render(request, "private_chats/private_chatroom.html",context)
@login_required
def search_results(request,*args,**kwargs):
    user=get_object_or_404(Profile,user_name=kwargs['username'])
    context={
        'user':user
    }
    if request.method=='GET':
           
        search_query = request.GET.get('to', None)
        if search_query:
            user_list = Profile.objects.filter(user_name__icontains=search_query)

    #user_list=Profile.objects.filter(user_name__isnull=True,user_name__icontains=query)
            context={   
            
            'user_list':user_list,
            'user':user
            }
        
    return render(request, "private_chats/search_results.html",context)


#return redirect("private_chats:chatroom",username=kwargs
#['username'])
      
@login_required
def MembersView(request,*args,**kwargs):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        members = Profile.objects.filter(user_name__icontains=url_parameter)
    else:
        members = Profile.objects.all()

    ctx["members"] = members
    if request.is_ajax():
        html = render_to_string(
        template_name="members-results-partial.html", 
        context={"members": members}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, "private_chats/newgroup.html", context=ctx)

@login_required
def create_group(request,*args,**kwargs):
    form=NewGroupForm
    if request.method=='POST':

        form=NewGroupForm(request.POST)
        if form.is_valid():
            admin_=get_object_or_404(Profile,id=request.user.profile.id)
            new_grp=form.save(commit=False)
            new_grp.admin=admin_

            new_grp.save()
            form.save_m2m()
            return redirect("private_chats:chatroom",username=kwargs['username'])
        else:
            form=NewGroupForm()
    else:
        form=NewGroupForm()

    context={
        'form':form
    }
        
    return render(request,'private_chats/newgroup.html',context)

@login_required
def GroupView(request,*args,**kwargs):
    msgs_received=PersonalMessages.objects.filter(msg_receiver=request.user.profile.id)
    contacts=PersonalMessages.objects.filter(msg_sender=request.user.profile.id)
    user=get_object_or_404(Profile,id=request.user.profile.id)
    my_groups=Group.objects.filter(admin=request.user.profile.id)
    groups=Group.objects.filter(members=request.user.profile.id)
    this_group=get_object_or_404(Group,id=kwargs['pk'])
    texts_sent_by_me=GroupMessages.objects.filter(sender=request.user.profile.id,grouproom=kwargs['pk'])
    texts=GroupMessages.objects.filter(grouproom=kwargs['pk'])
    form=GrpForm
    if request.method=='POST':
        form=GrpForm(request.POST)
        if form.is_valid():
            grp_msg=form.save(commit=False)
            grp_msg.sender=get_object_or_404(Profile,id=request.user.profile.id)
            grp_msg.grouproom=get_object_or_404(Group,id=kwargs['pk'])
            grp_msg.save()
            subject='New message'
            

        else:
            form=GrpForm()
    else:
        form=GrpForm()

    context={
        'user':user,
        'form':form,
        'contacts':contacts,
        'my_groups':my_groups,
        'groups':groups,
        'this_group':this_group,
        'texts_sent_by_me':texts_sent_by_me,
        'texts':texts,
        'msgs_received':msgs_received
    }
    return render(request,"private_chats/group_chats.html",context)


@login_required
def PrivateChatView(request,*args,**kwargs):
    user=get_object_or_404(Profile,id=request.user.profile.id)
    contacts=PersonalMessages.objects.filter(msg_sender=kwargs['pk'])
    msgs_received=PersonalMessages.objects.filter(msg_receiver=kwargs['pk'])
    texts_from=PersonalMessages.objects.filter(msg_sender=kwargs['pk'],msg_receiver=kwargs['pk_alt'])
    texts_to=PersonalMessages.objects.filter(msg_sender=kwargs['pk_alt'],msg_receiver=kwargs['pk'])
    receiver=get_object_or_404(Profile,id=kwargs['pk_alt'])
    my_groups=Group.objects.filter(admin=request.user.profile.id)
    groups=Group.objects.filter(members=request.user.profile.id)
    form=TxtForm
    if request.method=='POST':
        form=TxtForm(request.POST)
        if form.is_valid():
            
            txt=form.save(commit=False)
            txt.msg_sender=get_object_or_404(Profile,id=kwargs['pk'])
            txt.msg_receiver=get_object_or_404(Profile,id=kwargs['pk_alt'])
            txt.save()
            subject='New message'
            from_email=settings.EMAIL_HOST_USER
            to_email=txt.msg_receiver.email_id
            text_content="Hi, you have a new message!"
            html_content=get_template("private_chats/msg_received_email.html").render()
            msg= EmailMultiAlternatives(subject,text_content,from_email,[to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


        else:
            form=TxtForm()
    else:
        form=TxtForm()

    context={
    'user':user,
    'receiver':receiver,
    'texts_from':texts_from,
    'texts_to':texts_to,
    'form':form,
    'contacts':contacts,
    'my_groups':my_groups,
    'groups':groups,
    'msgs_received':msgs_received
    }

    return render(request,"private_chats/personal_chat.html",context)

@login_required
def group_details(request,*args,**kwargs):
    group=get_object_or_404(Group,id=kwargs['pk'])
    context={
        'group':group
    }
    return render(request,'private_chats/group_details.html',context)



'''

from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from direct.models import Message


from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

@login_required
def Inbox(request):
    messages = Message.get_messages(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))

@login_required
def UserSearch(request):
    query = request.GET.get("q")
    context = {}
    
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        #Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
                'users': users_paginator,
            }
    
    template = loader.get_template('direct/search_user.html')
    
    return HttpResponse(template.render(context, request))

@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct':active_direct,
    }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))


@login_required
def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('inbox')

@login_required
def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')
    
    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        Message.send_message(from_user, to_user, body)
        return redirect('inbox')
    else:
        HttpResponseBadRequest()

def checkDirects(request):
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message.objects.filter(user=request.user, is_read=False).count()

    return {'directs_count':directs_count}
'''