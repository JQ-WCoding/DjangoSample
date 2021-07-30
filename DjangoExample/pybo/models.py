from django.contrib.auth.models import User
from django.db import models


# 질문 게시글
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


# 답변 게시글
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # null 허용 (작성자 명 없음도 허용)
    modify_date = models.DateTimeField(null=True, blank=True)
