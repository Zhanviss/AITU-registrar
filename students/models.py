from django.db import models
from groups.models import Group
# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Student's ID", auto_created=True)
    first_name = models.CharField(verbose_name="Student's First Name", max_length=50)
    last_name = models.CharField(verbose_name="Student's Last Name", max_length=50)
    is_active = models.BooleanField(verbose_name="Student's Activity Status", default=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)
    student_email = models.CharField(verbose_name="Student's e-mail", max_length=255, unique=True)
    group_fk = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True
    )
    
    def __str__(self) -> str:
        return "Student: " + self.first_name + " "  + self.last_name