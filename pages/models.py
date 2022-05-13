from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    balance = models.IntegerField()
    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reciever')
    amount = models.IntegerField()
    def __str__(self):
        return f'{self.sender} has sent {self.amount} to {self.reciever}'