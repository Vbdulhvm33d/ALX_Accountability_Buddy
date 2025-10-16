from rest_framework import serializers
from .models import(Goals, JournalEntries, ProgressTrackers)
from django.contrib.auth.models import User

#note that our permisssions are defined in the views and viewsets not here!
#However, we can use the serializers to define our data validation and representation logic
#Also, we can use the serializers to define nested relationships between models if needed
#and we can use the serializers to define custom fields and methods for our models

class GoalsSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=Goals
        fields='__all__'


class JournalEntriesSerializer(serializers.ModelSerializer):
    goal=GoalsSerializer(read_only=True)
    user=serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=JournalEntries
        fields='__all__'

class ProgressTrackersSerializer(serializers.ModelSerializer):
    goal=GoalsSerializer(read_only=True) #many=True removed because it's a ForeignKey relationship and is only usedin many-to-many or one-to-many relationships
    user=serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=ProgressTrackers
        fields='__all__'
