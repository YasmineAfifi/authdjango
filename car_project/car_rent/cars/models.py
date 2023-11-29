from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator
# Create your models here.

class Car(models.Model):
    
    brand = models.CharField(max_length=30,validators=[MinLengthValidator(limit_value=3,message='Brand must be more than 3 char')])
    color = models.TextField(max_length=15,validators=[MinLengthValidator(limit_value=3,message='color must be more than 3 char') ,RegexValidator(regex=r'^[a-zA-Z]+$',message='Color accepts alphabets only')])
    price = models.DecimalField(max_digits=6,decimal_places=2) 
    image = models.ImageField(upload_to='./static/image/uploaded_image')

    def __str__(self) :
        
        return self.brand