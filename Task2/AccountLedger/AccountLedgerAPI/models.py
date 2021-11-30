from django.db import models

# Create your models here.
class AccountLedgerDetails(models.Model):
    account_name=models.CharField(max_length=30,default='')
    account_type=models.CharField(max_length=2,default='')
    amount=models.IntegerField(default=0)
    date=models.DateField()