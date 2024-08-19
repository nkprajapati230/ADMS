from django.db import models
import uuid

class bhulku(models.Model):

    # id = models.UUIDField(primary_key=True,default=uuid.uuid4 , editable=False, null=False)
    id=models.IntegerField(primary_key=True)

    first_name=models.CharField(max_length=24)
    middle_name=models.CharField(max_length=24)
    last_name=models.CharField(max_length=24)

    standard=models.SmallIntegerField(null=True)
    dob=models.DateField(default='2028-06-05')
    age=models.SmallIntegerField(null=True)

    school=models.CharField(max_length=24,null=True)
    phone_number=models.PositiveIntegerField(null=True)
    address=models.CharField(max_length=24,null=True)

    regular=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name+' '+self.last_name

