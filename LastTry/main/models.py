from django.db import models

data_db=[
    {'id':1,'name':'Борисыч','interes':'risovanie , football','price':'2000'},
    {'id':2,'name':'ktru','genre':'grid , fooll','price':'1000'},
    {'id':3,'name':'ktru','genre':'grid , fooll','price':'5'},
    {'id':4,'name':'ktru','genre':'grid , fooll','price':'100'},
    {'id':5,'name':'ktru','genre':'grid , fooll','price':'10'},
    {'id':6,'name':'ktru','genre':'grid , fooll','price':'1'},
    {'id':7,'name':'ktru','genre':'grid , fooll','price':'1000000'}
]

class Books(models.Model):
    name=models.TextField(blank=True)
    genre=models.TextField(blank=True)
    time_create= models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    price=models.IntegerField()

def __str__(self):
    return self.name
