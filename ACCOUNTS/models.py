from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class QuestionDetail(models.Model):
    Qid = models.CharField(max_length=20)
    QName = models.CharField(max_length=20)
    QAuthor = models.CharField(max_length=20)
    QDescription = models.CharField(max_length=20)
    TestCaseInput1 = models.TextField(max_length=200, blank='False')
    TestCaseInput2 = models.TextField(max_length=200, blank='False')
    Output1 = models.TextField(max_length=100, blank='False')
    Output2 = models.TextField(max_length=100, blank='False')
    Question = models.TextField(max_length=200)

    def __str__(self):
        return self.Qid;

class ProfessorDetail(models.Model):
    user = models.ForeignKey(User, unique=True,null=True)
    Batch = models.CharField(max_length=20)
    Qualification= models.TextField(max_length=20)
    Interest = models.TextField(max_length=200, blank='False')

    def __str__(self):
        return str(self.Batch)

