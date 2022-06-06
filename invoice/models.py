
from random import choices
from django.db import models
from django.conf import settings
from django.utils import timezone


#create initial invoice models

class clientAddress(models.Model):
    street =  models.CharField(null=True,max_length=200)
    city = models.CharField(null=True,max_length=200)
    postCode = models.CharField(null=True,max_length=200)
    country = models.CharField(null=True,max_length=200)
    
    def __str__(self):
        return f"{self.street} {self.postCode} {self.country}"

class senderAddress(models.Model):
    
    street =  models.CharField(null=True,max_length=200)
    city = models.CharField(null=True,max_length=200)
    postCode = models.CharField(null=True,max_length=200)
    country = models.CharField(null=True,max_length=200)
    
    def __str__(self):
        return f"{self.street} {self.postCode} {self.country}"


class Invoice(models.Model):
    
    
    status_options = [
                    ('Draft','Draft'),
                    ('Pending','Pending'),
                    ('Paid','Paid'),
                    ('','')
                    ]
    id = models.CharField(primary_key=True,max_length=200)   
    createdAt = models.DateTimeField(auto_now=True)
    paymentDue = models.DateField(blank=True, null=True)
    description = models.TextField(null=True)
    paymentTerms =  models.IntegerField(null=True)
    clientName = models.CharField(null =True,max_length=200)
    clientEmail = models.EmailField(null = True,max_length=200)
    status = models.CharField(max_length=10,choices=status_options,default='')
    total = models.FloatField(null=True,default=0.0)
    client_address = models.ForeignKey(clientAddress, on_delete=models.CASCADE,null=True,blank=True)
    sender_address = models.ForeignKey(senderAddress, on_delete=models.CASCADE,null=True,blank=True)
    
    def generate_id(self,length=10):
        """generate random string to be used as invoice id"""
        import string,random
        upper_string =  ''.join(random.choices(string.ascii_uppercase , k = 2))
        digit_string = ''.join(random.choices(string.digits , k = 4))

        rand_id =  upper_string + digit_string
        return rand_id
    
    
    def __str__(self):
        return self.id

    
    
    def generate_due_date(self,days=0):
        '''generate payment due date using payment terms'''
        from datetime import datetime,timedelta
        
        due_date = datetime.now() + timedelta(days=days)
        return due_date
    
    




    
class Items(models.Model):
    
    invoice = models.ForeignKey('Invoice',on_delete=models.PROTECT,null=True,blank=True)
    name =  models.CharField(null=True,max_length=200)
    quantity = models.PositiveIntegerField(null =True,max_length=200)
    price = models.PositiveIntegerField(null=True,max_length=200)
    total = models.PositiveIntegerField(null=True,max_length=200)
    
    def __str__(self):
        return self.name

    

   
"""{
    "id": "RT3080",
    "createdAt": "2021-08-18",
    "paymentDue": "2021-08-19",
    "description": "Re-branding",
    "paymentTerms": 1,
    "clientName": "Jensen Huang",
    "clientEmail": "jensenh@mail.com",
    "status": "paid",
    "senderAddress": {
      "street": "19 Union Terrace",
      "city": "London",
      "postCode": "E1 3EZ",
      "country": "United Kingdom"
    },
    "clientAddress": {
      "street": "106 Kendell Street",
      "city": "Sharrington",
      "postCode": "NR24 5WQ",
      "country": "United Kingdom"
    },
    "items": [
      {
        "name": "Brand Guidelines",
        "quantity": 1,
        "price": 1800.90,
        "total": 1800.90
      }
    ],
    "total": 1800.90
  },"""