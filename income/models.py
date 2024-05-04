from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
    
class Add_income(models.Model):
    source_type = {
        "Salary": "Salary",
        "Business": "Business",
        "Loan": "Loan",
        "Other": "Other",
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    source = models.CharField(choices=list(source_type.items()), max_length=20)
    date = models.DateField()

    def __str__(self):
        return self.source