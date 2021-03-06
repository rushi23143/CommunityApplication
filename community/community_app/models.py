from django.db import models

#Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)  
    email = models.CharField(max_length=150) 
    phone = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)

class Service(models.Model):
    service_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    service_provider_name = models.CharField(max_length=50, null=True, blank=True, default=None)
    contact_no = models.CharField(max_length=50, null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=0)
    posted_by = models.CharField(max_length=50, null=True, blank=True, default=None)

class Query(models.Model):
    que_category = models.CharField(max_length=50, null=True, blank=True, default=None)
    question = models.CharField(max_length=200, null=True, blank=True, default=None)
    approved = models.BooleanField(null=True, blank=True, default=False)
    posted_by = models.CharField(max_length=50, null=True, blank=True, default=None)


class Answer(models.Model):
    que_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    answer = models.TextField(max_length=500)
    posted_by = models.CharField(max_length=50, null=True, blank=True, default=None)

