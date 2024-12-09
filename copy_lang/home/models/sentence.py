from django.db import models

class Sentence(models.Model):
    text = models.TextField()  # 문장 텍스트
    audio_file = models.FileField(upload_to='audio_files/', null=True, blank=True)  # 음성 파일
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간

    def __str__(self):
        return self.text
