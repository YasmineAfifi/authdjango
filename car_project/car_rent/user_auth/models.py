from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Register(AbstractUser):
    name = models.CharField(max_length=30,validators=
                            [MinLengthValidator(limit_value=3, message='Name must be more than 3 char'),
                             RegexValidator(regex=r'^[a-zA-Z]+(\s[a-zA-Z]+)?$',message='Name accepts alphabets only')
                            ])
    
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=15,validators=[MinLengthValidator(limit_value=6,message="Password must be between 6 to 15 char")])
    username = None

    groups = models.ManyToManyField(
        Group,
        related_name='register_groups',
        related_query_name='group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='register_user_permissions',
        related_query_name='permission',
    )
    def __str__(self):

        return self.name


