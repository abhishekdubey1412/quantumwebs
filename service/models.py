from django.db import models

# Create your models here.
class Service(models.Model):
    type = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, null=True)
    content = models.TextField()

    def __str__(self):
        return self.type