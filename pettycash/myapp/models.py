from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
      pass
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('office', 'Office Supplies'),
        ('travel', 'Travel'),
        ('meal', 'Meals'),
        ('other', 'Other')
    ]
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - ₹{self.amount} - {self.submitted_by.username}"
    
class CashFloat(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.amount}"


class PettyCash(models.Model):
    total_cash = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Total Cash: ₹{self.total_cash}"
