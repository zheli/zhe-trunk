# Create your views here.
from django.core.urlresolvers    import reverse
from django.http                 import HttpResponseRedirect
from django.shortcuts            import get_object_or_404
from django.views.generic.simple import direct_to_template
from models                      import UploadFileForm, UploadFileModel
from FileHandling                import save_file
from filetransfers.api           import prepare_upload, serve_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #save_file(f)
            return HttpResponseRedirect('/')
    
    form = UploadFileForm()
    return direct_to_template(request, 'upload.html', 
            {'form': form})

def upload_handler(request):
    view_url = reverse('up5.upload_test.views.upload_handler')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadFileForm()
    return direct_to_template(request, 'upload2.html',
            {'form':form, 'upload_url': upload_url,
                'upload_data': upload_data,
                'uploads': reversed(UploadFileModel.objects.all())})

def download_handler(request, pk):
    upload = get_object_or_404(UploadFileModel, pk=pk)
    return serve_file(request, upload.file, save_as=False)

def delete_handler(request, pk):
    if request.method == 'POST':
        upload = get_object_or_404(UploadFileModel, pk=pk)
        upload.file.delete()
        upload.delete()
    return HttpResponseRedirect(reverse('up5.upload_test.views.upload_handler'))
