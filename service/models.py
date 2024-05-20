from django.db import models

# Create your models here.
class Service(models.Model):
    type = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.type