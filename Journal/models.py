from django.db import models
from django.contrib.auth.models import User
    

class Goals(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField(max_length=50, default='Not Started')
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JournalEntries(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
    goal=models.ForeignKey(Goals, on_delete=models.CASCADE, related_name='entries')
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    reflection_text=models.TextField()
    mood_rating=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Journal for {self.goal.title} on {self.date}"



class ProgressTrackers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprogress')
    goal=models.ForeignKey(Goals, on_delete=models.CASCADE, related_name='progress')
    completion_percentage=models.FloatField(default=0.0)
    streak_count=models.IntegerField(default=0)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.goal.title} - {self.completion_percentage}% complete"
                           
                           
# Create your models here.
