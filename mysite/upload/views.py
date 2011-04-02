from django.core.urlresolvers       import reverse
from django.contrib.auth.decorators import login_required
from django.http                    import HttpResponseRedirect
from django.shortcuts               import get_object_or_404, render_to_response
from django.template                import RequestContext
from django.views.generic.simple    import direct_to_template
from filetransfers.api              import prepare_upload, serve_file
from models                         import UploadForm, UploadModel

def upload_handler(request):
    view_url = reverse('upload.views.upload_handler')
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url, upload_data = prepare_upload(request, view_url, private=True)
    form = UploadForm()
    return direct_to_template(request, 'upload.html',
            {'form': form, 'upload_url':upload_url, 'upload_data':upload_data,
                'uploads':UploadModel.objects.all()})

def twitter_login(request):
    return render_to_response('social_login.html', RequestContext(request))


def download_handler(request, pk):
    if request.user.is_authenticated():
        upload = get_object_or_404(UploadModel, pk=pk)
        return serve_file(request, upload.file, save_as=False)
    else:
        view_url = reverse('books.views.hello')
        return HttpResponseRedirect(view_url)
