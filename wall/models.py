from django.db import models
from loginapp.models import User
import datetime
import re


# class UserManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 2:
#             errors["first_name"] = "First Name must be at least 2 characters"
#         if len(postData['last_name']) < 2:
#             errors["last_name"] = "Last Name must be at least 3 characters"
#         EMAIL_REGEX = re.compile(
#             r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = "Invalid email address!"
#         users = User.objects.all()
#         emaillist = []
#         for user in users:
#             emaillist.append(user.email)
#         if postData['email'] in emaillist:
#             errors['duplicate'] = "That email already exists"
#         if (datetime.date.today() < datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()):
#             errors['date'] = "Birthday must be in the past"
#         if (len(postData['password']) < 8):
#             errors['password'] = "Password must be at least 8 characters"
#         return errors
    
#     def login_validator(self, postData):
#         login_errors = {}
#         EMAIL_REGEX = re.compile(
#             r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):
#             login_errors['email'] = "Invalid email address!"
#         if (len(postData['password']) < 8):
#             login_errors['password'] = "Password must be at least 8 characters"
#         return login_errors

# User Class in login app for reference.
# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     birthday = models.DateField()
#     password = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()


class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message_id = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
