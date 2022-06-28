from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    link = models.CharField(max_length=300, default="")
    image = models.FilePathField(path="/img")

    def __str__(self):
        return f"{self.title} | {self.description}"
    
