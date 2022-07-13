from django.db import models

# Create your models here.
class Subject(models.Model):
    id = models.IntegerField(verbose_name="Subject's ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name="Subject's Title", max_length=120, unique=True)
    is_retake = models.BooleanField(verbose_name="Retaken status", default=False)

    def __str__(self) -> str:
        return "Subject: " + self.title