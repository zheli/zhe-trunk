# Create your views here.
from django.http import HttpResponse

def hello(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    ua = request.META.get('HTTP_USER_AGENT', 'unknow')
    return HttpResponse("page %s, is_secure: %s, ua: [%s], <table>%s</table>" % \
            (request.path, request.is_secure(), ua, '\n'.join(html)))
