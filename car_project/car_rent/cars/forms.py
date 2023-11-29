from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
       model = Car
       fields = '__all__'
       widgets ={
            'brand':forms.TextInput(attrs={"class":"registerInputs",'placeholder': 'Brand'}),
            'color':forms.TextInput(attrs={'class':'registerInputs','placeholder': 'Color'}),
            'price':forms.TextInput(attrs={'class':'registerInputs','placeholder': 'Price'}),
            'image':forms.FileInput(attrs={'class':'registerInputs'})
        }
       error_messages ={
           'brand':{
           'required':'Brand is Required',
           'max_length':'Brand must be less than 30 char'
          },
           'color':{
             'required':'Color is Required',
             
           },
           'price':{
             'required':'Price is Required',
           },
           'image':{
             'required':'Image Is Required',
           }
        }