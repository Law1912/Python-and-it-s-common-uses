from django.db import models

# Create your models here.
class Professors(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    research_interests = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name