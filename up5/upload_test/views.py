# Create your views here.
from django.http                 import HttpResponseRedirect
from django.shortcuts            import render_to_response
from django.views.generic.simple import direct_to_template
from models                      import UploadFileForm
from FileHandling                import save_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #save_file(f)
            return HttpResponseRedirect('/')

    else:
        form = UploadFileForm()
    return direct_to_template(request, 'upload_test/templates/upload.html', 
            {'form': form})
