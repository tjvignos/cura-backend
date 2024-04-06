from django.db import models

# Create your models here.

class Checkin(models.Model):
  id = models.AutoField(primary_key=True)
  date = models.DateField(null=True, blank=True)
  checked = models.BooleanField(default=False)
  response = models.TextField(blank=True, null=True)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  prompt = models.ForeignKey('prompt.Prompt', on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.user} - {self.date}'