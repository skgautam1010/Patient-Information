from django import forms
from django.forms import fields, widgets
from .models import Patient


GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Transgender','Transgender')
]


class PatientRegister(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'class':'form-check-input'}))
    class Meta:
        model=Patient
        fields=['first_name','last_name','gender','age','disease','doctor_name','fees','medicationdate','profile_img']
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'gender':'Gender',
            'age':'Age',
            'disease':'Disease',
            'doctor_name':'Doctor Name',
            'Fees':'Fees',
            'medicationdate':'Medication Date',
            'profile_img':'Image'
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'age': forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'disease': forms.TextInput(attrs={'class':'form-control','placeholder':'Disease'}),
            'doctor_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Doctors Name'}),
            'fees': forms.TextInput(attrs={'class':'form-control','placeholder':'Fees'}),
            'medicationdate': forms.DateInput(attrs={'class':'form-control datepicker','placeholder':'Medication Start Date Format (YYYY-MM-DD)'}),
            'profile_img':forms.FileInput(attrs={'class':'form-control'})
        }