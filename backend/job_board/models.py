from django.db import models

# Create your models here.
class Job(models.Model):
  title=models.CharField(max_length=150)
  company=models.CharField(max_length=150)
  link=models.CharField(max_length=500)
  job_id=models.CharField(max_length=150)

def __str__(self):
  return self.title