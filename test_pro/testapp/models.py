from django.db import models

# Create your models here.



class Testcases(models.Model):
    testid=models.IntegerField()
    testname=models.CharField(max_length=100)
    testcategory=models.CharField(default="MS1",max_length=30)

    def __str__(self):
        return str(self.testid)