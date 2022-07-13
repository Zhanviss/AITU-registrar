from django.db import models
from professors.models import Professor, ProfessorLinkPosition
# Create your models here.
class Subject(models.Model):
    id = models.IntegerField(verbose_name="Subject's ID", primary_key=True, auto_created=True)
    title = models.CharField(verbose_name="Subject's Title", max_length=120, unique=True)
    is_retake = models.BooleanField(verbose_name="Retaken status", default=False)

    def __str__(self) -> str:
        return "Subject: " + self.title

class SubjectLinkProfessor(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID of Subject and Professor combination", auto_created=True)
    professor_fk = models.ForeignKey(
        ProfessorLinkPosition,
        verbose_name="Professors of this Subject",
        on_delete=models.CASCADE
    )
    subject_fk = models.ForeignKey(
        Subject,
        verbose_name="Subjects of this Professor",
        on_delete=models.CASCADE,
    )
    def __str__(self) -> str:
        return self.professor_fk.__str__() +" " + self.subject_fk.__str__()