
from django.contrib import admin
from .models import QuestionDetail,ProfessorDetail,AssignmentDetail,CourseDetail,AssistantDetail

admin.site.register(QuestionDetail)
admin.site.register(ProfessorDetail)
admin.site.register(AssignmentDetail)
admin.site.register(CourseDetail)
admin.site.register(AssistantDetail)