from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','email','password']
        widgets ={
            'name':forms.TextInput(attrs={"class":"registerInputs",'placeholder': 'Your Full Name'}),
            'email':forms.EmailInput(attrs={'class':'registerInputs','placeholder': 'Email'}),
            'password':forms.PasswordInput(attrs={'class':'registerInputs','placeholder': 'Password'})
        }
        error_messages = {
            'name': {
                'required':"Name Is Required",
                'max_length':"Name must be less than 30 char"
            },
            'email':
            {   'required':'Email Is Required',
                'unique':'Email is already Exist'
            },'password':
            {
                'required':'Password Is Required',
                'max_length':'Password is more than 15 char'
            }
            
        }
        
   