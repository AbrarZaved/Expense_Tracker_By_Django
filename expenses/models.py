from django.db import models
import os
import json
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


<<<<<<< HEAD
=======

>>>>>>> af0cd1832d7c4fd2ea2a879ae605f836e197b9e7
class Add_expense(models.Model):
    category_type = {
        "Rent": "Rent",
        "Food": "Food",
        "Transport": "Transport",
        "Entertainment": "Entertainment",
        "Health": "Health",
        "Other": "Other",
    }
    
<<<<<<< HEAD
    
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
>>>>>>> af0cd1832d7c4fd2ea2a879ae605f836e197b9e7
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(choices=list(category_type.items()), max_length=20) 
    date = models.DateField()
    
    def __str__(self):
        return self.category
    
