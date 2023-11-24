from django.db import models

# Create your models here.
class Guitar(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
class GuitarData(models.Model):
    class Types: