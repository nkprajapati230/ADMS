from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from leaders.manager import leaderdbManager


class Leader(AbstractBaseUser):

    name=models.CharField(max_length=24,primary_key=True,unique=True)
    email=models.EmailField(max_length=255,blank=True,null=True)
    dob=models.DateField(null=True)
    can_edit=models.BooleanField(default=False)

    USERNAME_FIELD='name'
    REQUIRED_FIELDS=[]
    objects=leaderdbManager()

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True 


