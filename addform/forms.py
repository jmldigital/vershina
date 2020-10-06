from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customers
        exclude = ["customer_smms"]

        # class TextForm(forms.Form):
        #     body = forms.CharField(max_length=100)
        #
        #     def __init__(self, *args, **kwargs):
        #         super(TextForm, self).__init__(*args, **kwargs)
        #         self.fields['body'].widget.attrs.update({'class': 'form-control'})





class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass