from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_No = models.IntegerField()
    dname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    def __str__(self):
        return str(self.dept_No)
    
class Emp(models.Model):
    dept_No = models.ForeignKey(Dept,on_delete=models.CASCADE)
    emp_No = models.IntegerField()
    emp_Name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    mgr = models.IntegerField()
    hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField()
    email = models.EmailField(default='emp@gmail.com')
    def __str__(self):
        return self.emp_Name


class SalGrade(models.Model):
    grade = models.IntegerField()
    losal = models.IntegerField()
    hisal = models.IntegerField()
    def __str__(self):
        return self.grade
