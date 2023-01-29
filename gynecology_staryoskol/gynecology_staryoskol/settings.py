"""
Django settings for gynecology_staryoskol project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%za2a9)f_0pw9g)$s)r#&7i1&)w9r=ah-(3=xeq@d-1kh#2$!#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['gynecology-staryoskol.site','www.gynecology-staryoskol.site', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gynecology_app',
    'captcha'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gynecology_staryoskol.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'gynecology_staryoskol.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'u1815677_gynecology_db',
	    'USER': 'u1815677_gynecol',
	    'PASSWORD':'MaFgyn22.',
	    'HOST':'localhost',
    }
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

LANGUAGE_CODE = 'ru'


USE_I18N = True

USE_TZ = True

TIME_ZONE = 'Europe/Moscow'

TIME_ZONE = 'UTC'
DATETIME_FORMAT="H:i:s d.m.y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

STATIC_URL = '/staticfiles/'
base_static = Path(__file__).resolve().parent.parent.parent
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(base_static, 'staticfiles')
    ]
else:
    STATIC_ROOT = os.path.join(base_static, 'staticfiles')
BASE_URL="http://127.0.0.1:8000"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'vovatsar@bk.ru'
EMAIL_HOST_PASSWORD = 't9e0gD28KZW8wC9XtgNm'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

RECAPTCHA_PUBLIC_KEY = '6LfQ6NwjAAAAAGc9bnlaSxPvEHGx4OLMhsfO5EyV'
RECAPTCHA_PRIVATE_KEY = '6LfQ6NwjAAAAAEmaEOnIVulZsjwAuKN3BuNP3tNz'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5
RECAPTCHA_LANGUAGE = 'en'