from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

##########################################Assistant########################
class AssistantDetail(models.Model):
    #user = models.ForeignKey(User, unique=True,null=True)
    Batch = models.CharField(max_length=20)
    username = models.ForeignKey(User,null=True)
    CourseId= models.CharField(max_length=20, blank='False')
    TaId = models.CharField(max_length=20, blank='False')

    def __str__(self):
        return str(self.username)

############################################################################


class QuestionDetail(models.Model):
    Qid = models.CharField(max_length=20)
    QName = models.CharField(max_length=20)
    QAuthor = models.CharField(max_length=20)
    QDescription = models.CharField(max_length=20)
    Question = models.TextField(max_length=200)
    Image = models.FileField(null=True,blank=True)
    TestCaseInputFile1 = models.FileField(upload_to='documents/%Y/%m/%d',null=True)
    #file = models.FileField()

    def __str__(self):
        return self.Qid;

class ProfessorDetail(models.Model):
    #user = models.ForeignKey(User, unique=True,null=True)
    Batch = models.CharField(max_length=20)
    username = models.ForeignKey(User,null=True)
    Qualification= models.TextField(max_length=20)
    Interests = models.TextField(max_length=200, blank='False')

    def __str__(self):
        return str(self.username)


class StudentDetail(models.Model):
    username = models.ForeignKey(User,null=True)
    SiD = models.CharField(max_length=20)
    Batch=models.CharField(max_length=20)
    Branch=models.CharField(max_length=20)
    Programme=models.CharField(max_length=20)

    def __str__(self):
        return str(self.username)



class AssignmentDetail(models.Model):
    AssignmentID = models.CharField(max_length=20,null=True)
    CreationDate = models.DateField(max_length=20)
    StartTime =  models.DateTimeField()
    EndTime =  models.DateTimeField()
    Courseid = models.CharField(max_length=20)
    Description = models.TextField(max_length=200)
    Language = models.CharField(max_length=20)

    def __str__(self):
        return str(self.AssignmentID)

class CourseDetail(models.Model):
    CourseName=models.CharField(max_length=20,null=False)
    CourseId=models.CharField(max_length=20,null=False)
    Description=models.TextField(max_length=200)
    PId=models.CharField(max_length=20)
    StartDate= models.DateField(null=True)
    EndDate= models.DateField(null=True)
    Semester=models.IntegerField(null=False)
    Year=models.CharField(max_length=4)

    def __str__(self):
        return str(self.CourseId)

