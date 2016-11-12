
from django.contrib import admin
from .models import QuestionDetail,ProfessorDetail,AssignmentDetail,CourseDetail\
    ,AssistantDetail,Assignment_languages,StudentDetail,Submission,Course_student,Courses_Ta,AssignmentQuestion


admin.site.register(QuestionDetail)
admin.site.register(ProfessorDetail)
admin.site.register(AssignmentDetail)
admin.site.register(CourseDetail)
admin.site.register(AssistantDetail)
admin.site.register(Courses_Ta)
admin.site.register(Course_student)
admin.site.register(Submission)
admin.site.register(StudentDetail)
admin.site.register(Assignment_languages)
admin.site.register(AssignmentQuestion)
