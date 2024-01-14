from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc  = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.fname
class Job_list_Contact(models.Model):
    fname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.fname
# Create your models here.

