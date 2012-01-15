import sys

try:
    sys.modules['socket'] = __import__('btsocket')
except ImportError:
    pass

from appuifw import *
import os, inspect
import e32
import struct
import camera
import httplib, urllib2, socket
from httplib import NotConnected

import logging
logging.getLogger().setLevel(logging.DEBUG)
ROOT_PATH = os.path.dirname(inspect.getfile(inspect.currentframe()))

import mimetypes
import sysinfo

# don't modify this part
# Modified from
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/146306
def post_multipart(host, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTPConnection(host)  
    headers = {
        'User-Agent': sysinfo.sw_version(),
        'Content-Type': content_type
        }
    h.request('POST', selector, body, headers)
    res = h.getresponse()
    return res.status, res.reason, res.read()

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    # No need to URL encode as this is form text data.
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    # ''.join() won't work here (PyS60 doesn't like it), so we do it
    # with a virtual file.
    from cStringIO import StringIO
    file_str = StringIO()
    for i in range(len(L)):
        file_str.write(L[i])
        file_str.write(CRLF)
    body = file_str.getvalue()
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    # we should guess the type, but since its not in our PyS60
    # distribution, we will just say octet.
    # return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    return 'application/octet-stream'
#external library ends

ip = '192.168.0.35'
new_line = u'\u2029'

class Daemon(object):
    def __init__(self):
        self.lock = e32.Ao_lock()
        self.dir = "e:\\"
        self.apo = None
        self.port = 54321
        app.title = u'Daemon'
        app.screen = 'normal'
        app.menu = [(u'About', self.about)]
        self.body = Text()
        app.body = self.body
        self.lock = e32.Ao_lock()

    def sel_access_point(self):
        """ Select and set the default access point.
        Return the access point object if the selection was done or None if not
        """
        aps = socket.access_points()
        if not aps:
            note(u"No access points available","error")
            return None
 
        ap_labels = map(lambda x: x['name'], aps)
        item = popup_menu(ap_labels,u"Access points:")
        if item is None:
            return None
        logging.debug('AP set: %s' % item)
        apo = socket.access_point(aps[item]['iapid'])
        socket.set_default_access_point(apo)
        return apo

    def get_signal(self, cs, addr):
        data = ""
        name = ""
        size = 0
        while True:
            n = data.find("\n")
            if n >= 0:
                command = data[:n]
                break
            try:
                buf = cs.recv(1024)
            except socket.error:
                cs.close()
                return
            data = data + buf

        self.body.add(u'Received command %s' % command + new_line)
        if command == 'take_photo':
            take_photo()
        else:
            pass
        cs.close()

    def server(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((ip, port))
        except socket.error, (val,msg):
            note(u'Error %d: %s' % (val,msg), 'info')
            return

        s.listen(1)

        while True:
            (cs, addr) = s.accept()
            self.body.add(u'Connect to %s:%d' % (addr[0], addr[1]) + new_line)
            self.get_signal(cs, addr)

    def about(self):
        note(u'This is about', 'info')

    def run(self):
        self.apo = self.sel_access_point()
        #self.apo = True
        if self.apo:
            self.apo.start()
            self.body.add(u'Starting server.' + new_line)
            #self.body.add(u'IP = %s' % self.apo.ip() + new_line)
            self.body.add(u'IP = %s' % ip + new_line)
            self.body.add(u'Port = %d' % self.port + new_line)
            self.server(ip, self.port)
            #self.server(self.apo.ip(), self.port)
            #app.exit_key_handler=quit
            self.lock.wait()
        app.set_exit()

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('192.168.0.1', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def take_photo():
    resolution=(1024,768)
    zoom=1
    img=camera.take_photo('RGB', resolution, zoom)
    picture_path = os.path.join(ROOT_PATH, 'picture.jpg')
    logging.debug(picture_path)
    img.save(picture_path, quality=100)
    logging.info("Photo took!")
    try:
        upload_picture()
    except urllib2.TypeError:
        pass
    logging.info('Photo uploaded!')

def upload_picture():
    register_openers()
    host = '192.168.0.34'
    path = '/api/'
    url = 'http://192.168.0.34/api/'
    f = open(os.path.join(ROOT_PATH, 'picture.jpg'), 'rb')
    f_content = f.read()
    f.close()
    fields = []
    files = [('data', 'picture.jpg', f_content)]
    logging.info(post_multipart(host, path, fields, files))
    #datagen, headers = multipart_encode({
    #            'file':open(os.path.join(ROOT_PATH, 'picture.jpg'), 'rb')
    #        })
    #request = urllib2.Request(url, datagen, headers)
    #result = urllib2.urlopen(request)
    #print(result.read())

def quit(self):
    logging.info('App exited')
    app_lock.signal()
    app.set_exit()

if __name__ == "__main__":
    app = Daemon()
    while True:
        try:
            app.run()
        except:
            logging.error('Some errors, exit...')
            pass