from django.db import models
from django.conf import settings
from django.dispatch import receiver
# from django_comments_xtd.signals import should_request_be_authorized

class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True) # this means it is optional
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    # author = models.CharField(max_length=50)
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

class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.CharField(max_length=60)
    job_title = models.CharField(max_length=120)
    job_description = models.CharField(max_length=200)
    salary = models.FloatField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=False)
    


  
# def ma_callback(sender, comment, request, **kwargs):
#     if((request.user and request.user.is_authenticated) or 
#        (request.auth and request.auth == settings.MY_DRF_AUTH_TOKEN)):
#         return True

    
# class Comments(models.Model):
    
#     author = models.CharField(max_length=50)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.author}"
    
    
