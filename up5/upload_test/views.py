# Create your views here.
from django.core.urlresolvers       import reverse
from django.contrib.auth            import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http                    import HttpResponseRedirect
from django.shortcuts               import get_object_or_404, render_to_response
from django.template                import RequestContext
from django.views.generic.simple    import direct_to_template
from models                         import UploadFileForm, UploadFileModel
from FileHandling                   import save_file
from filetransfers.api              import prepare_upload, serve_file
from social_auth.backends           import BACKENDS, OpenIdAuth, BaseOAuth, BaseOAuth2

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

@login_required
def upload_handler(request):
    view_url = reverse('up5.upload_test.views.upload_handler')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url)
    form = UploadFileForm()
    print(request.user.social_auth.get().extra_data)
    return direct_to_template(request, 'upload2.html',
            {'form':form, 'upload_url': upload_url,
                'upload_data': upload_data,
                'uploads': reversed(UploadFileModel.objects.all()),
                'user': request.user.social_auth.all()})

def download_handler(request, pk):
    upload = get_object_or_404(UploadFileModel, pk=pk)
    return serve_file(request, upload.file, save_as=False)

def delete_handler(request, pk):
    if request.method == 'POST':
        upload = get_object_or_404(UploadFileModel, pk=pk)
        upload.file.delete()
        upload.delete()
    return HttpResponseRedirect(reverse('up5.upload_test.views.upload_handler'))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/test/upload2/')
    else:
        return render_to_response('home.html', RequestContext(request))
