from tokenize import group
from django.db import models
from students.models import Student
from subjects.models import Subject
from groups.models import  Group
from professors.models import Professor
# Create your models here.
class Report(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Report ID", auto_created=True)
    student_1to1 = models.OneToOneField(
        Student,
        on_delete= models.CASCADE,
        verbose_name="Student Reported"
    )
    subject_1to1 = models.OneToOneField(
        Subject,
        on_delete=models.CASCADE,
        default = None,
        null=True,
        verbose_name="Subject of Student Reported"
    )
    professor_1to1 = models.OneToOneField(
        Professor,
        on_delete=models.CASCADE,
        default = None,
        null=True,
        verbose_name="Professor of Student Reported"
    )
    group_1to1 = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Group"
    )
    is_active = models.BooleanField(default=True, verbose_name="Activity")
    document_pdf = models.FileField(verbose_name="Electronic Version of Document")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date")
    def __str__(self) -> str:
        return self.student_1to1.__str__() + " " + self.student_1to1.group_fk.__str__()