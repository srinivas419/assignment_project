from django.db import models


# Create your models here.

class courses_table(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_fee = models.IntegerField()
    c_duration = models.CharField(max_length=50)


# class LogInPage(models.Model):
#     first_name = models.CharField(max_length=250, unique=True, help_text="Please enter first name")
#     last_name = models.CharField(max_length=250, null=True, blank=True, help_text="Please enter last name")
#     mobile_no = models.CharField(max_length=20, unique=True, help_text=" Enter your mobile number")
