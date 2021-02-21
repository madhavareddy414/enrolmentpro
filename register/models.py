from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30)
    saddr = models.CharField(max_length=30)
    sdep = models.CharField(max_length=30)
    ssch = models.CharField(max_length=30)

    def __str__(self):
        return self.sname

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.ename

class EmpSalary(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

    def __str__(self):
        return self.ename

