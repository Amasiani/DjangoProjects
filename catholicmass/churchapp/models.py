from django.db import models

# Create your models here.
class Diocese(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Parish(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=80)
    location = models.PointField()

    def __str__(self):
        return " %s, %s" (self.name, self.location)