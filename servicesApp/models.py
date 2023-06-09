from django.db import models
from django.utils import timezone # Import timezone for DateTimeField
from django.contrib.auth.models import User # Import User model

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    service_Main_Img = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=2000)
    provider = models.ForeignKey(User, on_delete=models.CASCADE) # If a user created the post is deleted, posts are deleted as well.ß

    # __str__() method returns how the Post is printed
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'service'

