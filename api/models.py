from django.db import models

 # Create your models here.

    

class ContactMessage(models.Model):
     name= models.CharField(max_length=255)
     email = models.EmailField()
     msg = models.TextField()

     def __str__(self):
    #     # return f"{self.name or 'No Name'}({self.email or 'No Email'})"
         return self.name