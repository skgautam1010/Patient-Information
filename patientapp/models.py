from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    contact=models.BigIntegerField()
    emailid=models.EmailField(max_length=30)
    feedback=models.CharField(max_length=500)

    def __str__(self):
        return self.first_name