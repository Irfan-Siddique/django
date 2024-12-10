from django import forms
from django.core import validators
class contactForm(forms.Form):

    file=forms.FileField()
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label = "User Email")
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # email=forms.EmailField()
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    # check=forms.BooleanField()
    # birthday=forms.DateField()
    # appoinment=forms.DateTimeField()

    # CHOICES=[('S', 'small'),('M', 'Medium'),('L','Large')]
    # size=forms.ChoiceField(choices=CHOICES)
    
    # TOPINGS=[('P', 'Pepperoni'),('M', 'Mashroom'),('B','Beef')]
    # pizza=forms.MultipleChoiceField(choices=TOPINGS)

# class studentForm(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("at least 10 char")
#     #     return valname
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("use .com")
#     #     return valemail

#     def clean(self):
#         cleaned_data= super().clean()
#         valname= self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("at least 10 char")
#         if '.com' not in valemail:
#             raise forms.ValidationError("use .com")


def len_check(value):
    if len(value) <10:
        raise forms.ValidationError("enter a value more than 9 chars")

class studentForm(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(10, message='not more than 10 chars')])
    email=forms.CharField(widget=forms.EmailInput,
        validators=[validators.EmailValidator(message="Enter a valid Email")])
    
    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),
                    validators.MinValueValidator(24, message="age must be at least 24")])
    
    file= forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='pdf & png only')])

    text = forms.CharField(
        widget=forms.TextInput, validators=[len_check])

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")