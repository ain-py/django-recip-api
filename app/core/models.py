"""
Databse models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for users."""
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('User must have an Email')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None):
        """ Create and return a superUser"""
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    """ User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager() # assigning usermanager class to user 
    USERNAME_FIELD = 'email' # replace defualt username filed with email
