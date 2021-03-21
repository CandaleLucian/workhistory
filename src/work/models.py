from django.db import models


# Create your models here.
class Work(models.Model):
    project = models.CharField(max_length=120)  # max length = required
    hours = models.DecimalField(decimal_places=1, max_digits=12)
    work_descriptions = models.TextField(blank=True, null=True)
    date = models.DateField()
