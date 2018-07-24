from django.db import models

from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class employers(models.Model):
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=70)
    email = models.EmailField(null= False, unique=True)
    phone = models.CharField(null= False, max_length=14, validators=[MinLengthValidator(14)])
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.firstname
