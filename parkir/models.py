from django.db import models

class Parkir(models.Model):
    Title = models.CharField(max_length=50)
    Status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title