from django.db import models
from shared_app.models import SweetType

# Create your models here.
class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
    
