# Create your views here.
from django.core.urlresolvers       import reverse
from django.http                    import HttpResponseRedirect
from models                         import UploadForm, UploadModel

def upload_handler(request):
    view_url    = reverse('upload.views.upload_handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILE)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url, private=True)
    form = UploadForm()
    return direct_to_template(request, 'upload.html',
            {'form':form, 'upload_url':upload_url, 'upload_data':upload_data,
                'uploads':UploadMOdel.objects.all(), 'names':names})
