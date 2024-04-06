from django.db import models

# Create your models here.

class Circle(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  users = models.ManyToManyField('auth.User', related_name='circles')

  def __str__(self):
    return self.name