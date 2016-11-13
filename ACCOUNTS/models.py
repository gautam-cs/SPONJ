from django.db import models
from django.contrib.auth.models import User

class StudentDetail(models.Model):
    SId = models.CharField(primary_key=True,max_length=20,null=False)
    Batch=models.CharField(max_length=20,null=False)
    Branch=models.CharField(max_length=20,null=False)
    Name=models.CharField(max_length=30,null=False)
    Email = models.EmailField()
    Password=models.CharField(max_length=20,null=False)
    Programme=models.CharField(max_length=20,null=False)

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
    CourseId = models.CharField(max_length=20, null=False)
    Year = models.CharField(max_length=4,null=False)
    CourseName=models.CharField(max_length=20,null=False)
    Description=models.TextField(max_length=200,null=False)
    PId=models.ForeignKey(ProfessorDetail,max_length=20,null=False)
    StartDate= models.DateField(null=False)
    EndDate= models.DateField(null=False)
    Semester=models.CharField(max_length=10,null=False)

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
    Qid = models.CharField(primary_key=True,max_length=20)
    QName = models.CharField(max_length=20,null=False)
    QAuthor = models.CharField(max_length=20,null=False)
    QDescription = models.CharField(max_length=20,null=False)
    Image = models.ImageField(upload_to = 'images/albums/',null=False)
    TestCaseInputFile1 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    TestCaseInputFile2 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    OutputFile1 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)
    OutputFile2 = models.FileField(upload_to='documents/%Y/%m/%d',null=False)

class AssignmentDetail(models.Model):
    AssignmentID = models.CharField(primary_key=True,max_length=20,null=False)
    AssignmentName = models.CharField(max_length=20,null=True)
    CreationDate = models.DateField(null=False)
    StartTime =  models.DateTimeField(null=False)
    EndTime =  models.DateTimeField(null=False)
    Courseid = models.ForeignKey(CourseDetail,max_length=20,null=False)
    Description = models.TextField(null=False)
    Language = models.CharField(max_length=20)

    def __str__(self):
        return str(self.AssignmentID)

class AssignmentQuestion(models.Model):
    QId=models.ForeignKey(QuestionDetail,null=False,max_length=20)
    AId=models.ForeignKey(AssignmentDetail,null=False,max_length=20)

class Submission(models.Model):
    SubmissionId=models.CharField(primary_key=True,max_length=20)
    StudentId=models.ForeignKey(StudentDetail,null=False)
    AssignmentId=models.ForeignKey(AssignmentDetail,null=False)
    QuestionId=models.ForeignKey(QuestionDetail,null=False)
    PercentagePass=models.IntegerField()
    Result=models.CharField(max_length=20)
    SubmissionTime=models.DateTimeField()
    StdOutError=models.TextField(null=True)

    def __str__(self):
        return self.Qid;

class Courses_Ta(models.Model):
    CourseId=models.ForeignKey(CourseDetail,null=False)
    TaId=models.ForeignKey(AssistantDetail,null=False)

class Course_student(models.Model):
    SId=models.ForeignKey(StudentDetail,to_field='SId',null=False)
    CourseId=models.ForeignKey(CourseDetail,null=False)


class Assignment_languages(models.Model):
    AssignmentId=models.ForeignKey(AssignmentDetail,null=False)
    Programming_Language=models.CharField(max_length=20,null=True)
