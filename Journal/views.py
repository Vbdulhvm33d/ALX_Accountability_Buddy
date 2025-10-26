#from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions, generics
from .serializers import GoalsSerializer, JournalEntriesSerializer, ProgressTrackersSerializer, UserSerializer
from .models import Goals, JournalEntries, ProgressTrackers
from django.contrib.auth.models import User
from Journal.permissions import isOwnerorReadonly


class registerUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

    def perform_create(self, serializer):
        user=serializer.save()
        token, _ = TokenAuthentication.objects.get_or_create(user=user)
        self.Token=token

    def create(self, request, *args, **kwargs):
        response=super().create(request, *args, **kwargs)
        response.data['token']=self.Token.key
        return response
            
class BaseUserViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated, isOwnerorReadonly]

    #this line of function ensures that the user field is automatically 
    # set to the currently authenticated user when a new goal is created.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    #this line of function filters the queryset to only include goals 
    # that belong to the currently authenticated user. 
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
