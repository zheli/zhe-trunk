AUTHENTICATION_BACKENDS = (
        'social_auth.backends.twitter.TwitterBackend',
        'django.contrib.auth.backends.ModelBackend',
)
LOGIN_REDIRECT_URL = '/upload/'
TWITTER_CONSUMER_KEY = 'LSoo2bS4EvtqLtfhWI9Ug'
TWITTER_CONSUMER_SECRET = 'OkJjh6dsqCNNMdXGq6O1qUTmOyrUOLRT0eW7JScHN8Y'
FACEBOOK_APP_ID = '147599935286264'
FACEBOOK_API_SECRET = '67ddd22dc4cc41dfde941f5207fc9b10'
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_KEY = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
SOCIAL_AUTH_CREATE_USERS = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'complete'
LOGIN_ERROR_URL = '/login/error/'
#SOCIAL_AUTH_USER_MODEL = 'app.CustomUser'
SOCIAL_AUTH_ERROR_KEY = 'socialauth_error'
