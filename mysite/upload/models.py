from django.db  import models
from django     import forms

class UploadModel(models.Model):
    title = models.CharField(max_length=64, blank=True)
    file = models.FileField(upload_to='uploaded_files/%Y-%m-%d/')

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
