from os.path import join, normpath
from .base import *

######## PROJECT DEPLOYMENT VARIABLES
from .deployment_variables import PROJECT_SECRET_KEY
from .deployment_variables import PROJECT_DATABASE_NAME
from .deployment_variables import PROJECT_DATABASE_USER
from .deployment_variables import PROJECT_DATABASE_PASS
from .deployment_variables import PROJECT_DATABASE_HOST

######### END PROJECT DEPLOYMENT VARIABLES


########## DEBUG CONFIGURATION
DEBUG = True
TEMPLATE_DEBUG = True
########## END DEBUG CONFIGURATION


ALLOWED_HOSTS = ['notes.vandorjw.me.localhost',]
SITE_URL = 'http://notes.vandorjw.me.localhost'


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT_DATABASE_NAME,
        'USER': PROJECT_DATABASE_USER,
        'PASSWORD': PROJECT_DATABASE_PASS,
        'HOST': PROJECT_DATABASE_HOST,
        'PORT': 5432,
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
INSTALLED_APPS += (
    'debug_toolbar',
)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END TOOLBAR CONFIGURATION

######### BrowserID
LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGOUT_REDIRECT_URL = '/'
BROWSERID_AUDIENCES = ['https://notes.vandorjw.me.localhost',]
######### End Browser ID

SECRET_KEY = PROJECT_SECRET_KEY
