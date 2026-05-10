from django.db import models

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    image = models.ImageField(upload_to='', blank=True, null=True)
    degree = models.DecimalField(decimal_places=2,max_digits=4,null=False)
    
    def __str__(self):
        return self.name