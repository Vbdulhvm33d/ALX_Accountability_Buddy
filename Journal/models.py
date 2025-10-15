from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    ID=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    

class Goals(models.Model):
    ID=models.AutoField(primary_key=True)
    userID=models.ForeignKey(Users, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class JournalEntries(models.Model):
    userID=models.ForeignKey(Users, on_delete=models.CASCADE)
    goalID=models.ForeignKey(Goals, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    reflection_text=models.TextField()
    moodrating=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)



class ProgressTrackers(models.Model):
    ID=models.AutoField(primary_key=True)
    userID=models.ForeignKey(Users, on_delete=models.CASCADE)
    goalID=models.ForeignKey(Goals, on_delete=models.CASCADE)
    completion_percentage=models.FloatField()
    streak_count=models.IntegerField()
    last_updated=models.DateTimeField(auto_now=True)
                           # Create your models here.
