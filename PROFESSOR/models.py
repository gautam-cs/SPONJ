from django.db import models
from django.utils import timezone


class QuestionDetail(models.Model):
    Qid=models.CharField(max_length=20)
    Question = models.TextField(max_length=200)
    #Qid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Qid;
