from django.db import models
import os
import json
from django.conf import settings

# Create your models here.
currency = []
file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
open(file_path, 'r')
with open(file_path, 'r') as json_file:
    data = json.load(json_file)
    for key, value in data.items():
        currency.append((key, f"{key}-{value}"))


class Add_Expense(models.Model):
    category_type = {
        "Rent": "Rent",
        "Food": "Food",
        "Transport": "Transport",
        "Entertainment": "Entertainment",
        "Health": "Health",
        "Other": "Other",
    }
    
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(choices=currency)
    description = models.TextField()
    category = models.CharField(choices=list(category_type.items()))
    date = models.DateField()
    
    def __str__(self):
        return self.category