from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('newmessage', views.newmessage),
    path('newcomment/<int:messageid>', views.newcomment),
    path('deletecomment/<int:commentid>', views.deletecomment),
    path('deletemessage/<int:messageid>', views.deletemessage)
]
