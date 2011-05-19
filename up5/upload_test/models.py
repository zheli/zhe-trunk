from django.forms import ModelForm
from django.db    import models

# Create your models here.
class UploadFileModel(models.Model):
    title = models.CharField(max_length = 60, blank=True)
    file  = models.FileField(upload_to = 'file/%d')

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFileModel
