from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import GoalsSerializer, JournalEntriesSerializer, ProgressTrackersSerializer
from .models import Goals, JournalEntries, ProgressTrackers
from django.contrib.auth.models import User

#class BaseUserViewset(viewsets.ModelViewSet):
    #permission_classes=[permissions.IsAuthenticated]
    #def perform_create(self, serializer):
        #return serializer.save(user=self.request.user)
    
    #def get_queryset(self):
        #return self.queryset.filter(user=self.request.user)

class GoalsViewSet(viewsets.ModelViewSet):
    queryset=Goals.objects.select_related('user').all()
    serializer_class=GoalsSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):#this line of function ensures that the user field is automatically set to the currently authenticated user when a new goal is created.
        serializer.save(user=self.request.user)

    def get_queryset(self):#this line of function filters the queryset to only include goals that belong to the currently authenticated user.
        return self.queryset.filter(user=self.request.user)
    
class JournalEntriesViewSet(viewsets.ModelViewSet):
    queryset=JournalEntries.objects.select_related('user','goal').all()
    serializer_class=JournalEntriesSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class ProgressTrackersViewSet(viewsets.ModelViewSet):
    queryset=ProgressTrackers.objects.select_related('user','goal').all()#I included select_related to optimize queries by reducing the number of database hits when accessing related user and goal objects.
    serializer_class=ProgressTrackersSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    




# Create your views here.
