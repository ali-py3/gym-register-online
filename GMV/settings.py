"""
Django settings for GMV project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
LOGIN_REDIRECT_URL = '/'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf.global_settings import LOGGING

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*^1m2)vlw%)v@=w++$ur%zmi#!gfzwimqa30jtp9lfo1=$3y5f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gym_register',
    'azbankgateways',
    'widget_tweaks'
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

ROOT_URLCONF = 'GMV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'GMV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os

AUTH_USER_MODEL = 'gym_register.User'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       # 'BMI': {
       #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
       #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
       #     'SECRET_KEY': '<YOUR SECRET CODE>',
       # },
       # 'SEP': {
       #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
       #     'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
       # },
       # 'ZARINPAL': {
       #     'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
       # },
       'IDPAY': {
           'MERCHANT_CODE': '6797544c-a7fd-42d1-b3cf-ae93177cebc4',
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       },
   #     'ZIBAL': {
   #         'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
   #     },
   #     'BAHAMTA': {
   #         'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
   #     },
   #     'MELLAT': {
   #         'TERMINAL_CODE': '<YOUR TERMINAL CODE>',
   #         'USERNAME': '<YOUR USERNAME>',
   #         'PASSWORD': '<YOUR PASSWORD>',
   #     },
   },
   'DEFAULT': 'IDPAY',
   'CURRENCY': 'IRT', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 5, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   # 'BANK_PRIORITIES': [
   #     'BMI',
   #     'SEP',
   #     # and so on ...
   # ], # اختیاری
}
