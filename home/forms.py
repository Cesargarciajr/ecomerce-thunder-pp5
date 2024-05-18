from django import forms
from .models import contactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactMessage
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone

    # Transform input field to textarea
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget = forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your message here'})