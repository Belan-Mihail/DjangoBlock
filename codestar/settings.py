"""
Django settings for codestar project.

Generated by 'django-admin startproject' using Django 3.2.21.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from django.contrib.messages import constants as messages
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["django-block-heroku-0ea39cb4833e.herokuapp.com", "localhost", "8000-belanmihail-djangoblock-v4kb8gz7460.ws-eu104.gitpod.io", "8000-belanmihail-djangoblock-v4kb8gz7460.ws-eu105.gitpod.io",]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'blog',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',

#     and we can add in the all auth apps that we've  just installed so first of all we need to
# add django.contrib.sites this is a built-in  django package and then our all auth packages
# so all auth all auth dot account  and all auth dot social account
]

SITE_ID = 1
# we also need to add a site id of one this  is so that django can handle multiple sites
# from one database now of course we only  have one site here using our one database
# but we'll still need to explicitly tell django  the site number so site underscore id equals one

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# and we'll add in the redirection  urls too so that after we've logged
# in all logged out the site will  redirect us to the home page
# so log in redirect url equals forward slash we'll  just copy that and then change login to log out

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
    }
# And now further down in the  file, we can assign the tags.
# What do we mean by this?
# Well each message has a built-in tag to  indicate the category of the message -
# is it a warning or an error? Is it indicating a  success or is it just giving info to the user?
# We want to assign these tags  to different Bootstrap classes  
# so that the color of our message will  change according to its category.

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# We'll also tell Crispy to use  Bootstrap classes for formatting. 
# So: CRISPY_TEMPLATE_PACK = 'bootstrap4' .

# Installing django_summernote
# pip3 install django_summernote
# pip3 freeze --local > requirements.txt
# add to app 'django_summernote',
# in urls.py: path('summernote/',  include('django_summernote.urls')),
# make migration

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'codestar.wsgi.application'

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/



 
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

