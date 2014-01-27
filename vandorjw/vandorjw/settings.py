import os
#
# PROJECT SECRETS
#
from .secrets import PROJECT_SECRET_KEY
from .secrets import PROJECT_DATABASE_NAME
from .secrets import PROJECT_DATABASE_USER
from .secrets import PROJECT_DATABASE_PASS
from .secrets import PROJECT_DATABASE_HOST
#
# END PROJECT SECRETS
#


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['vandorjw.me','notes.vandorjw.me',]

EXTERNAL_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    'crispy_forms',
    'tinymce',
    'south',
)

LOCAL_APPS = (
   'blog',
   'contact',
)

INSTALLED_APPS = EXTERNAL_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vandorjw.urls'

WSGI_APPLICATION = 'vandorjw.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PROJECT_DATABASE_NAME,
        'USER': PROJECT_DATABASE_USER,
        'PASSWORD': PROJECT_DATABASE_PASS,
        'HOST': PROJECT_DATABASE_HOST,
        'PORT': '5432',
    }                                             
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


########## STATIC FILE CONFIGURATION
STATIC_ROOT =  '/var/sites/me/vandorjw/assets/'
STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    '/var/sites/me/vandorjw/src/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    '/var/sites/me/vandorjw/src/vandorjw/templates',
)
########## END TEMPLATE CONFIGURATION

########## SECRET CONFIGURATION
SECRET_KEY = PROJECT_SECRET_KEY
########## END SECRET CONFIGURATION

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
}
