from django.db import models

# Create your models here.

class Prompt(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateField(null=True, blank=True)
  text = models.TextField()

  def __str__(self):
    return self.text