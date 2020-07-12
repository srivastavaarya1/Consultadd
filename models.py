from django.db import models

# Create your models here.
#class candidates(models.Model):
#    candidateId = models.Charfeild(max_length =20)
#    firstname = models.Charfeild(max_length = 10)

#class Candidate(models.Model):
#    name = models.CharField(unique=False, max_length=50)
#    contact = models.IntegerField(unique=True)
#    email = models.EmailField(unique=True)

#    def __str__(self):
#        return self.name

class Employee(models.Model):
    EmployeeID = models.CharField(max_length=50)
    EmployeeName = models.CharField(max_length=50)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)

    class Meta:
        ordering = ['EmployeeID']

    def __str__(self):
        return self.EmployeeName
