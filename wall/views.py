from django.shortcuts import render, redirect
from django.contrib import messages
from loginapp.models import User
from .models import Message, Comment
import datetime
import bcrypt

def check_for_methodPOST(request):
    if request.method != 'POST':
        return redirect('/')    

def check_for_user(request):
    if not 'userid' in request.session:
        return redirect('/')
    else:
        global logged_in_user 
        logged_in_user = User.objects.get(email=request.session['userid'])

def deletemessage(request, messageid):
    check_for_user(request)
    message_to_delete = Message.objects.get(id=messageid)
    if logged_in_user.id == message_to_delete.user_id.id:
        message_to_delete.delete()
    else:
        messages.error(request, "Only message writers can delete messages!")
    return redirect('/wall')

def deletecomment(request, commentid):
    check_for_user(request)
    comment_to_delete = Comment.objects.get(id=commentid)
    parent_message = comment_to_delete.message_id
    if (logged_in_user.id == comment_to_delete.user_id.id) or (logged_in_user.id == parent_message.user_id.id):
        comment_to_delete.delete()
    else:
        messages.error(request, "Only comment writers or message writers can delete comments!")
    return redirect('/wall')

def newmessage(request):
    check_for_user(request)
    check_for_methodPOST(request)
    Message.objects.create(user_id = User.objects.get(email=request.session['userid']),  message = request.POST['newmessagetext'])
    return redirect('/wall')

def newcomment(request, messageid):
    check_for_user(request)
    check_for_methodPOST(request)
    Comment.objects.create(user_id = User.objects.get(email=request.session['userid']), message_id = Message.objects.get(id=messageid),  comment = request.POST['newcomment'])
    return redirect('/wall')

def wall(request):
    check_for_user(request)
    context = {
        "logged_in_user": logged_in_user,
        "users" : User.objects.all(),
        "wallmessages" : Message.objects.all(),
        "comments" : Comment.objects.all(),
        "usermessages" : logged_in_user.messages.all()
    }
    return render(request, "wall.html", context)
