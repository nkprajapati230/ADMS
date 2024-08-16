from django.contrib.auth.models import BaseUserManager


class leaderdbManager(BaseUserManager):

    def create_user(self, name, email, dob, password=None):

        if not name:
            raise ValueError('Name field cannot be empty')
        
        user=self.model(
            name=name,
            email=self.normalize_email(email),
            dob=dob,
        )
    
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, name, password=None):

        if not name:
            raise ValueError('Name field cannot be empty')
        
        user=self.model(
            name=name
        )
         
        user.set_password(password)
        user.save(using=self.db)
        
        return user


