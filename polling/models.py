from django.db import models
from django.utils import timezone 
import datetime 

class Question(models.Model): 
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date publish')
    def __str__(self): 
        return self.question_text
    def recent_changes(self): 
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model): 
   
    questions = models.ForeignKey(Question, on_delete=models.CASCADE) 
    
    choice_text = models.CharField(max_length=150) 
    
    votes = models.IntegerField(default=0)
    
    def __str__(self): 
        return self.choice_text