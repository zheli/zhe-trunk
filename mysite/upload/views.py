from django.core.urlresolvers       import reverse
from django.http                    import HttpResponseRedirect
from django.views.generic.simple    import direct_to_template
from filetransfers.api              import prepare_upload
from models                         import UploadForm

def upload_handler(request):
    view_url = reverse('upload.views.upload_handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadForm()
    return direct_to_template(request, 'upload.html',
            {'form': form, 'upload_url':upload_url, 'upload_data':upload_data})
