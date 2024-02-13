from django.db import models

# Create your models here.
class SweetType(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
