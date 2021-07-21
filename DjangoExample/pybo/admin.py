from django.contrib import admin

# Register your models here.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']  # 제목과, 내용으로 검색하기


admin.site.register(Question, QuestionAdmin)
