from django.db import models

class Parkir(models.Model):
    Title = models.CharField(max_length=50)
    Status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Title

class Jumlah(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    Tersedia = models.IntegerField(default=1)
    
    def __str__(self):
        return self.id
