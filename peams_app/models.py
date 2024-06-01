from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


# Create your models here.
class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    batch_no = models.CharField(max_length=50, unique=True)
    expired = models.BooleanField(default=False)
    about_to_expire = models.BooleanField(default=False)
    alert_status = models.CharField(default="okay", max_length=20)

    def __str__(self):
        return F"{self.name} with batch no: {self.batch_no}"
    
    def save(self, *args, **kwargs):
    # Generate a random alphanumeric string for batch_no
        self.batch_no = ''.join([
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_uppercase),
        '_',
        str(random.randint(100, 999))
        ])
        super().save(*args, **kwargs)
        
