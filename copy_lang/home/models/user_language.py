from django.db import models
from django.contrib.auth.models import User
from .language import Language

class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.language.name}"
