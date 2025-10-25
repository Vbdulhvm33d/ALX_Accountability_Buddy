#from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, permissions, generics
from .serializers import GoalsSerializer, JournalEntriesSerializer, ProgressTrackersSerializer
from .models import Goals, JournalEntries, ProgressTrackers
from django.contrib.auth.models import User
from Journal.permissions import isOwnerorReadonly

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class BaseUserViewset(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, isOwnerorReadonly]
    def perform_create(self, serializer):#this line of function ensures that the user field is automatically set to the currently authenticated user when a new goal is created.
        serializer.save(owner=self.request.user)

   #this line of function filters the queryset to only include goals that belong to the currently authenticated user. 
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(user=user)
        return self.queryset.none()

class GoalsViewSet(BaseUserViewset):
    queryset=Goals.objects.select_related('user').all()
    serializer_class=GoalsSerializer
    #permission_classes=[permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)

    #def get_queryset(self):
        #return self.queryset.filter(user=self.request.user)
    
class JournalEntriesViewSet(BaseUserViewset):
    queryset=JournalEntries.objects.select_related('user','goal').all()
    serializer_class=JournalEntriesSerializer
    #permission_classes=[permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)

    #def get_queryset(self):
        #return self.queryset.filter(user=self.request.user)
    
class ProgressTrackersViewSet(BaseUserViewset):
    queryset=ProgressTrackers.objects.select_related('user','goal').all()#I included select_related to optimize queries by reducing the number of database hits when accessing related user and goal objects.
    serializer_class=ProgressTrackersSerializer
    #permission_classes=[permissions.IsAuthenticated]

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)

    #def get_queryset(self):
        #return self.queryset.filter(user=self.request.user)
    




# Create your views here.
