
from django.db import models
import datetime
from django.utils import timezone

bestfriend = (
    ("yes","yes"),
    ("No","No"),
    ("Hell NO","Hell NO"),
    ("its complicated","its complicated")
)
class Friends(models.Model):
    First_Name = models.CharField(max_length=20)
    Second_Name = models.CharField(max_length=20)
    Third_Name = models.CharField(max_length=20)
  
    Mobile_Number  = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    Are_You_My_Bestfriend = models.CharField(choices=bestfriend, null=True, default="yes",max_length=100)
    
    def __str__(self):
        return self.First_Name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text