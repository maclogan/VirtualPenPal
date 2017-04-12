from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SavedText(models.Model):
    ENGLSIH = "en"
    MANDARIN = "zh-CN"
    LANG_CHOICES = (
        (ENGLSIH, 'english'),
        (MANDARIN, 'mandarin'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=5, choices = LANG_CHOICES, default='english')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True);

    def __str__(self):
        return self.text
