from django.db import models


#
# # Create your models here.
class FreeTriler(models.Model):
    windoid=models.CharField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    start=models.DateField()
    expire=models.DateField()
    finish=models.BooleanField(default=False)

