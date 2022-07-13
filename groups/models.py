from django.db import models
from subjects.models import SubjectLinkProfessor
# Create your models here.

class Group(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Group's ID", auto_created=True)
    group_name = models.CharField(verbose_name="Group's Name", max_length=50, unique=True)
    is_active = models.BooleanField(verbose_name="Group's Activity Status", default=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)

    def __str__(self) -> str:
        return "Group: " + self.group_name

class GroupLinkProfessorSubject(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID of Group and Professor+Subject combination", auto_created=True)
    group_fk = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="ID of Group"
    )
    prof_subj_fk = models.ForeignKey(
        SubjectLinkProfessor,
        on_delete=models.CASCADE,
        verbose_name="ID of Subject and Professor combination"
    )
    term_count = models.IntegerField(verbose_name="The term's number", default=1)
    academ_year = models.CharField(verbose_name="ACADEM YEAR", default="FORMAT: yyyy - yyyy", max_length=30, unique=True)
    is_active = models.BooleanField(verbose_name="Combination's Activity Status", default=True)

    def __str__(self) -> str:
        return self.group_fk.__str__() + " " + self.prof_subj_fk.__str__() + f"Academ year: {self.academ_year}, term count:{self.term_count} "