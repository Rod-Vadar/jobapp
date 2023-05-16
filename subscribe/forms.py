from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter your email'),
        }
        # Does not work in for loop in subscribe
        # help_texts={
        #     'first_name':_('Enter characters only')
        # }
        error_messages={
            'first_name':{
                'required':_('You must enter first name')
            },
            'last_name':{
                'required':_('You must enter last name')
            },
            'email':{
                'required':_('You must enter email')
            },
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid ',' found in form ")
#     return value

# class SubscribeForm(forms.Form):
#     first_name=forms.CharField(max_length=100, required=False, label="Enter first name", help_text="Enter characters only")
#     last_name=forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     email=forms.EmailField(max_length=100)

