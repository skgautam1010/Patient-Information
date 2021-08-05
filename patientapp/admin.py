from django.contrib import admin
from .models import Contact,Patient
# Register your models here.



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','gender','age','disease','doctor_name','fees','medicationdate')



admin.site.register(Contact)