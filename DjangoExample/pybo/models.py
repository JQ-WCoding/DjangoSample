from django.contrib.auth.models import User
from django.db import models


# 질문 게시글
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 생성일
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # 작성자
    modify_date = models.DateTimeField(null=True, blank=True)  # 날짜 변경
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천

    def __str__(self):
        return self.subject


# 답변 게시글
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='author_answer')
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # null 허용 (작성자 명 없음도 허용)
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  # 추천


# 댓글
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
