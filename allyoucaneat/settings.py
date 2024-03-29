"""
Django settings for allyoucaneat project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import sys
import django_heroku
import dj_database_url
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG",True,cast=bool)

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS= ["https://allyoucaneat.up.railway.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'customers',
    'custom_user',
    'products',
    'vendors',
    'orders',
    'receipts',
    'sasapay',
    'feedback',
    # '',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
]

ROOT_URLCONF = 'allyoucaneat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'templates',
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

WSGI_APPLICATION = 'allyoucaneat.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT= BASE_DIR/'staticfiles'
STATICFILES_DIRS= [BASE_DIR/'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom user
AUTH_USER_MODEL= "custom_user.User"

# settings variables
CURRENCY= config("CURRENCY")

CLIENT_ID= config("CLIENT_ID")
CLIENT_SECRET= config("CLIENT_SECRET")
SASAPAY_HEAD_URL= config("SASAPAY_HEAD_URL")

CALLBACK_URL= "%s" %(config("CALLBACK_URL"))
TOKEN_URL= "%s%s" %(config("SASAPAY_HEAD_URL"),config("TOKEN_URL"))
PAYMENT_REQUEST= "%s%s" %(config("SASAPAY_HEAD_URL"),config("PAYMENT_REQUEST"))
PROCESS_PAYMENT= "%s%s" %(config("SASAPAY_HEAD_URL"),config("PROCESS_PAYMENT"))
TRANSACTION_STATUS= "%s%s" %(config("SASAPAY_HEAD_URL"),config("TRANSACTION_STATUS"))
VERIFY_TRANSACTION= "%s%s" %(config("SASAPAY_HEAD_URL"),config("VERIFY_TRANSACTION"))
NETWORK_CODE= config("NETWORK_CODE")

# allow external access
CORS_ALLOW_ALL_ORIGINS= True

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Switch Databases
DEVELOPMENT_MODE= config("DEVELOPMENT_MODE",cast=bool)
if DEVELOPMENT_MODE:
    # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dballyoucaneat',
            'USER': 'postgres',
            'PASSWORD': 'PostgreSQL23!@#',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASE_URL = config("DATABASE_URL")
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
    }