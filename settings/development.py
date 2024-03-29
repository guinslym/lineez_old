import os

from .base import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'p-h93iwrvc0+3e%m9)8(b(ml1clqwih^u=7p%p+o$ln$^458kn'

DEBUG=True
TEMPLATE_DEBUG_MODE = True

DEV_APPS = (
    'debug_toolbar',
    'django_seed',
)
INSTALLED_APPS = BASE_APPS + DEV_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    

)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# LOGGING
LOGGING = {
     'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '[%(asctime)s] %(levelname)s : %(message)s'
         },
         'verbose': {
             'format': '[%(asctime)s] %(levelname)s %(filename) % : %(message)s'
         },
     },
     'handlers': {
         'file': {
             'level': 'INFO',
             'class': 'logging.FileHandler',
             'formatter': 'verbose',
             'filename': BASE_DIR+'/logs/dev.log',
             'mode': 'a',
         },
     },
     'loggers': {
         'django': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'applications.delivrem.views': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'applications.delivrem.utils': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
         'applications.delivrem.tweets': {
             'handlers': ['file'],
             'level':'INFO',
             'propagate': True,
         },
     },
 }

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
