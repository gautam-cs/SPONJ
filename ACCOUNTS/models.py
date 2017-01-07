from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class StudentDetail(models.Model):
    prog=(
        ('select', 'select'),
        ('B-tech','B-tech'),
        ('M-tech','M-tech'),
    )

    branch=(
        ('select', 'select'),
        ('CS','Computer Science'),
        ('IT','Information Techonology'),
    )

    batch=(
        ('select', 'select'),
        ('2013-17','2013-17'),
        ('2014-18','2014-18'),
        ('2015-19','2015-19'),
        ('2016-20','2016-20'),
    )

    SId = models.CharField(primary_key=True,max_length=20,null=False)
    Batch=models.CharField(max_length=20,choices=batch,default='select')
    Branch=models.CharField(max_length=20,choices=branch,default='select')
    Name=models.CharField(max_length=30,null=False)
    Email = models.EmailField()
    Password=models.CharField(max_length=20,null=False)
    Programme=models.CharField(max_length=20,choices=prog,default='select')

    def __str__(self):
        return str(self.SId)

class ProfessorDetail(models.Model):
    PId = models.CharField(primary_key=True,max_length=20,null=False)
    Name=models.CharField(max_length=20,null=False)
    Email= models.EmailField()
    Password=models.CharField(max_length=20,null=False)
    Qualification= models.TextField(max_length=20,null=False)
    Interests = models.TextField(max_length=200,null=False)

    def __str__(self):
        return str(self.PId)

class CourseDetail(models.Model):
    sem=(
        ('select', 'select'),
        ('Autumn','Autumn'),
        ('Winter','Winter')
    )

    year=(
        ('datetime.now().year','datetime.now().year'),
        ('select','select'),
    )

    CourseId = models.CharField(max_length=20, null=False)
    Year = models.CharField(max_length=20,choices=year,default='select')
    CourseName=models.CharField(max_length=20,null=False)
    Description=models.TextField(max_length=200,null=False)
    PId=models.ForeignKey(ProfessorDetail,max_length=20,null=False)
    StartDate= models.DateField(default=timezone.now)
    EndDate= models.DateField(default=timezone.now)
    Semester=models.CharField(max_length=20,choices=sem,default='select')

    class Meta:
        unique_together=('CourseId','Year')
    
    def __str__(self):
        return str(self.CourseId)
    

class AssistantDetail(models.Model):
    TaId = models.CharField(primary_key=True,max_length=20,null=False)
    Name = models.CharField(max_length=20,null=False)
    Email = models.EmailField()
    CourseId= models.ForeignKey(CourseDetail,max_length=20,null=False)
    Password=models.CharField(max_length=20,null=False)


    def __str__(self):
        return str(self.TaId)


class QuestionDetail(models.Model):
    QName = models.CharField(max_length=20,null=False)
    QAuthor = models.CharField(max_length=20,null=False)
    QDescription = models.CharField(max_length=20,null=False)
    Image = models.ImageField(upload_to = 'images/albums/',null=False)
    TestCaseInputFile1 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    TestCaseInputFile2 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    OutputFile1 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    OutputFile2 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)

    def __str__(self):
        return self.QName;

class AssignmentDetail(models.Model):
    AssignmentName = models.CharField(max_length=20,null=True)
    CreationDate = models.DateField(null=False, default=date.today())
    StartTime =  models.DateTimeField(null=False)
    EndTime =  models.DateTimeField(null=False)
    Courseid = models.ForeignKey(CourseDetail,max_length=20,null=False)
    Description = models.TextField(null=False)

    def __str__(self):
        return self.AssignmentName

class AssignmentQuestion(models.Model):
    QId=models.ForeignKey(QuestionDetail,null=False,max_length=20)
    AId=models.ForeignKey(AssignmentDetail,null=False,max_length=20)

    def __str__(self):
        return self.id;

class Submission(models.Model):
    StudentId=models.ForeignKey(StudentDetail,null=False)
    AssignmentId=models.ForeignKey(AssignmentDetail,null=False)
    QuestionId=models.ForeignKey(QuestionDetail,null=False)
    PercentagePass=models.IntegerField()
    Result=models.CharField(max_length=20)
    SubmissionTime=models.DateTimeField()
    StdOutError=models.TextField(null=True)

    def __str__(self):
        return str(self.id);


class Courses_Ta(models.Model):
    CourseId=models.ForeignKey(CourseDetail,null=False)
    TaId=models.ForeignKey(AssistantDetail,null=False)

    def __str__(self):
        return self.CourseId;

class Course_student(models.Model):
    SId=models.ForeignKey(StudentDetail,to_field='SId',null=False)
    CourseId=models.ForeignKey(CourseDetail,null=False)

    def __str__(self):
        return self.CourseId;


class Assignment_languages(models.Model):
    AssignmentId=models.ForeignKey(AssignmentDetail,null=False)
    Programming_Language=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.id;
