from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    
    def __str__(self):
        return self.title + self.description