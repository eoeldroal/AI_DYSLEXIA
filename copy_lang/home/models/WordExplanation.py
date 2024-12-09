from django.db import models

class WordExplanation(models.Model):
    word = models.CharField(max_length=1500, primary_key=True)
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)  # 오디오 파일 경로
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.word
