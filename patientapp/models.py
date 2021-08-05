from django.db import models

# Create your models here.



class Patient(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=60)
    age=models.IntegerField()
    disease=models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=50)
    fees=models.IntegerField(default=500)
    medicationdate=models.DateField()
    profile_img=models.ImageField(upload_to="profileimg",default="profile_image.jpg",blank=True)


class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    contact=models.IntegerField()
    emailid=models.EmailField(max_length=30)
    feedback=models.CharField(max_length=500)

    def __str__(self):
        return self.first_name