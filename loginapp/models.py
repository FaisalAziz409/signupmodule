from django.db import models

# Create your models here.
class signup(models.Model):
    email=models.CharField(max_length=100)
    password=models.IntegerField()
    address=models.CharField(max_length=255)
    address1=models.CharField(max_length=255)
    mobile_number=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()

    def __str__(self):
        return self.email