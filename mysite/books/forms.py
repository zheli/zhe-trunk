from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email   = forms.EmailField(required=False)
    message = forms.CharField()

class UploadFileForm(forms.Form):
    title   = forms.CharField(max_length=50)
    file    = forms.FileField()
