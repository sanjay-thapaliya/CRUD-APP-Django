from django.db import models

# Create your models here.

class Blog(models.Model):
    first = models.CharField(max_length=1000)


