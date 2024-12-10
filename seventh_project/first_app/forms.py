from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        # fields=['name','roll']
        fields='__all__'
        # exclude=['roll']

        labels={'name':'Student name', 'roll': 'Student Roll'}



        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }