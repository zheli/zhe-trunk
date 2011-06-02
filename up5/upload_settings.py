PREPARE_UPLOAD_BACKEND      = 'filetransfers.backends.default.prepare_upload'
#Use Django to serve files
SERVE_FILE_BACKEND          = 'filetransfers.backends.default.serve_file'
#Use X-Sendfile to serve files
#SERVE_FILE_BACKEND          = 'filetransfers.backends.xsendfile.serve_file'
#Use this if you have a base URL for public downloads
PUBLIC_DOWNLOAD_URL_BACKEND = 'filetransfers.backends.default.public_download_url'
#PUBLIC_DOWNLOADS_BASE_URL = '/gridfs/'
