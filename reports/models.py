from django.db import models
from students.models import Student
# Create your models here.
class Report(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Report ID", auto_created=True)
    student_1to1 = models.OneToOneField(
        Student,
        on_delete= models.CASCADE
    )
    
    is_active = models.BooleanField(default=True, verbose_name="Activity")
    document_pdf = models.FileField(verbose_name="Electronic Version of Document")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date")

    def __str__(self) -> str:
        return self.student_id.__str__() + " Created at: " + str(self.created_date) + " Modified at: " + str(self.modified_date)