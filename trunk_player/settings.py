"""
Django settings for trunk_player project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$)ntjbvj=my84lgkn8(vr13f#pz4uu&ai_mhp=ys9imph%cgeq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'local_override',
    'radio.apps.RadioConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.instagram',
    'rest_framework',
    'channels',
    'pinax.stripe',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'radio.custom_middleware.ExtendUserSession',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trunk_player.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trunk_player.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "audio_files"),
#]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 50
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "audio_files")

# Channel settings
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "radio.routing.channel_routing",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'django': {
            'handlers': ['mail_admins',],
            'propagate': True,
            'level': 'ERROR',
        },
        'radio': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}

# How far back an anonymous user can see back in minutes
# 0 will disable the limit
ANONYMOUS_TIME = 15

# This Agency must exist in radio.Agency 
RADIO_DEFAULT_UNIT_AGENCY = 0

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}

ACCOUNT_AUTHENTICATION_METHOD="username_email"
ACCOUNT_EMAIL_REQUIRED=True
LOGIN_REDIRECT_URL="/"

AMAZON_ADDS = False
AMAZON_AD_TRACKING_ID = 'scanoc-20'
AMAZON_AD_LINK_ID = '366e01afa07db536277fa926bed3cb27'
AMAZON_AD_EMPHASIZE_CATEGORIES = '15684181,13900871,172282,3760901,16310091,229534'
AMAZON_AD_FALL_BACK_SEARCH = ['fire extinguisher', 'first aid',]

GOOGLE_ANALYTICS_PROPERTY_ID = '0'

TWITTER_ACTIVE = False
TWITTER_LIST_URL = None

SITE_TITLE = 'Trunk-Player'
SITE_EMAIL = 'help@example.com'

PINAX_STRIPE_SECRET_KEY = '0'
PINAX_STRIPE_PUBLIC_KEY = '0'

# Set this to the location of your audio files
AUDIO_URL_BASE = '//s3.amazonaws.com/SET-TO-MY-BUCKET/'

# Which settings are passed into the javascript object js_config
JS_SETTINGS = ['SITE_TITLE', 'AUDIO_URL_BASE']

# Which settings are aviable to the template tag GET_SETTING
VISABLE_SETTINGS = ['SITE_TITLE', 'AUDIO_URL_BASE', 'GOOGLE_ANALYTICS_PROPERTY_ID', 'COLOR_CSS', 'SITE_EMAIL', 'PINAX_STRIPE_PUBLIC_KEY', 'TWITTER_ACTIVE', 'TWITTER_LIST_URL']

ALLOW_ANONYMOUS = False

PINAX_STRIPE_SECRET_KEY = 'sk_test_xxxxxxxxxxxxxxxxxxxx'
PINAX_STRIPE_PUBLIC_KEY = 'pk_test_xxxxxxxxxxxxxxxxxxxx'
PINAX_STRIPE_INVOICE_FROM_EMAIL = 'help@example.com'

ACCESS_TG_RESTRICT = False


# Load our local settings 
try:
    LOCAL_SETTINGS
except NameError:
    try:
        from trunk_player.settings_local import *
    except ImportError:
        print("Failed to open settings_local.py")

