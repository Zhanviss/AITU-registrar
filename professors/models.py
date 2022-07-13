from django.db import models

# Create your models here.
class Professor(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Professor's ID", auto_created=True)
    first_name = models.CharField(verbose_name="Professor's First Name", max_length=50)
    last_name = models.CharField(verbose_name="Professor's Last Name", max_length=50)
    is_active = models.BooleanField(verbose_name="Professor's Activity Status", default=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)
    professor_email = models.CharField(verbose_name="Professor's e-mail", max_length=255, unique=True)
    
    def __str__(self) -> str:
        return "Professor: " + self.first_name + " " + self.last_name

class JobPosition(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Professor job position's ID", auto_created=True)
    title = models.CharField(verbose_name="Title of job", max_length=20)

    def __str__(self) -> str:
        return "Position: " + self.title

class ProfessorLinkPosition(models.Model):
    id = models.IntegerField(verbose_name="ID of Professor and Position combination", primary_key=True, auto_created=True)
    is_active = models.BooleanField(verbose_name="Combination's Activity Status", default=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)
    professor_fk = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        verbose_name="ID of professor"
    )
    position_fk = models.ForeignKey(
        JobPosition,
        on_delete=models.CASCADE,
        verbose_name="ID of position"
    )

    def __str__(self) -> str:
        return self.professor_fk.__str__() + " " + self.position_fk.__str__()