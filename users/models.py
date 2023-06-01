from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from datetime import datetime, timedelta
import random

stock_type = (
    ('A', 'STOCK A'),
    ('B', 'STOCK B'),
    ('C', 'STOCK C'),
    ('D', 'STOCK D'),
)
class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    User = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Avatar = models.ImageField(default='/img/download.png', upload_to='profile pictures')

class Profit_loss(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    profit = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.now()
        else:
            self.timestamp += timedelta(minutes=1)
        super().save(args, **kwargs)

    def generate_PL(self):
        self.profit = random.uniform(30, 75)
        self.loss = random.uniform(-30, 100)

class Details(models.Model):
    Initial_Deposit = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    Trader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Balance = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    stock_type = models.CharField(max_length=2, default='A', choices=stock_type)
