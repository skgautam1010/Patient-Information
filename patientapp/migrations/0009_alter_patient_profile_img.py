# Generated by Django 3.2.6 on 2021-08-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0008_alter_patient_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profile_img',
            field=models.ImageField(blank=True, default='images/profile_image.jpg', upload_to='images/'),
        ),
    ]
