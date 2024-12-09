from django.db import models
from .sentence import Sentence

class Question(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    question_text = models.TextField()  # 생성된 질문 텍스트
    answer = models.TextField(null=True, blank=True)  # 사용자가 입력한 답변

    def __str__(self):
        return self.question_text
