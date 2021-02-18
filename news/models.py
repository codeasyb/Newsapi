from django.db import models

# Create your models here.

class Article(models.Model):
    
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200) 
    body = models.TextField()
    location = models.CharField(max_length=100)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    # The field will automatically get set once the new instnace of a model is created [auto_now_add]
    created_at = models.DateTimeField(auto_now_add=True)
    # automatically the instance is saved [auto_now] 
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return f"{self.author} {self.title}"