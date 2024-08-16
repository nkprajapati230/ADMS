from django.db import models

class bhulku(models.Model):
    first_name=models.CharField(max_length=24)
    middle_name=models.CharField(max_length=24)
    last_name=models.CharField(max_length=24)

    standard=models.SmallIntegerField(null=True)
    dob=models.DateField(null=True)
    age=models.SmallAutoField(null=True)

    school=models.CharField(max_length=24,null=True)
    address=models.CharField(max_length=24,null=True)
