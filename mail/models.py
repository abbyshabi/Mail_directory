from __future__ import unicode_literals
from django.db import models

class User(models.Model):
   """
   This is the class we will use to create images
   """
   
   First_Name = models.CharField(max_length = 50)
   Last_Name = models.CharField(max_length = 50)
   Email = models.TextField(max_length=100)
   
   def save_user(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()