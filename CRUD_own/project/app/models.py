from django.db import models

# Create your models here.
class Company(models.Model):
    emp_id = models.IntegerField(unique=True, blank=True)
    emp_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    salary = models.IntegerField(blank=True)
    joining_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.emp_name