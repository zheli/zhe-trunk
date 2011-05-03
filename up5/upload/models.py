from django.db import models
from django    import forms

# Create your models here.

class UploadModel(models.Model):
    title   = models.CharField(max_length=64, blank=True)
    file    = models.FileField(upload_to='uploaded_files/%Y-%m-%d/')

    @property
    def filename(self):
        return self.file.name.resplit('/', 1)[-1]

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
