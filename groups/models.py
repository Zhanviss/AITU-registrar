from django.db import models

# Create your models here.

class Group(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Group's ID", auto_created=True)
    group_name = models.CharField(verbose_name="Group's Name", max_length=50, unique=True)
    is_active = models.BooleanField(verbose_name="Group's Activity Status", default=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="Modified Date", auto_now=True)

    def __str__(self) -> str:
        return "Group: " + self.group_name