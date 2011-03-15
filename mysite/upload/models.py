from django.db  import models
from django     import forms

class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/%Y-%m-%d/')

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
