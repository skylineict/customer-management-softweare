from django import forms
from django.core.validators import validate_email
from .models import Bulkemail


class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)


class myform(forms.ModelForm):
    Emailto = MultiEmailField()

    class Meta:
        model = Bulkemail
        fields = ('Emailto',)
        widgets = {
            "Emailto": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "full name here"}), }
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     recipients = MultiEmailField()
#     cc_myself = forms.BooleanField(required=False)
