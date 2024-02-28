"""
Django settings for ecomerce_thunder project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@b061v=4=0us57nip)7gv#+4%uen2h=_*a^)x!rit@zbgqnq)l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8000-cesargarcia-ecomercethu-h0clgdzew2r.ws-eu108.gitpod.io',
                '8000-cesargarcia-ecomercethu-h0clgdzew2r.ws-eu108.gitpod.io',
                'thunder-nutrition-6bac86cc4153.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'products',
    'shopping_cart',
    'checkout',
    'profiles',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # required by allauth
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

ROOT_URLCONF = 'ecomerce_thunder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), # wiring up root template directory and custom allauth templates directory
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth', # required by allauth
                'django.contrib.messages.context_processors.messages',
                'shopping_cart.contexts.shopping_cart_contents', # content processor for shopping cart content
            ],
        },
    },
]

# Django-Allauth backends needed settings
CSRF_TRUSTED_ORIGINS = ['https://8000-cesargarcia-ecomercethu-h0clgdzew2r.ws-eu108.gitpod.io'] # Required by Django 4 update https://docs.djangoproject.com/en/dev/releases/4.0/#format-change

# Toasts Messages storage
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'



AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Allauth email confirmation settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'ecomerce_thunder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe Settings
FREE_DELIVERY = 35
STANDARD_DELIVERY = 15
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = 'pk_test_51OmPWUI8NvNINQ7FUSsIoYm6FsgdeACAJ1UJtpX5FFVYcsqlUnr8CYWL6oKUxaRNj8EIVGcwqF8pUJlFFa9T0Fd500Vg9iABpQ'
STRIPE_SECRET_KEY = 'sk_test_51OmPWUI8NvNINQ7Fy55CSLbchccuFkEP6aovwH2k8xTFXPj6NYDuLhDa1jXv608hJ8QV7FtptrHud7jnNO7BJeT1008lnVR3tW'
STRIPE_WH_SECRET = 'whsec_g0lbVvv0vwYxzUImbEe3znFrh2PaWsMw'

DEFAULT_FROM_EMAIL = 'thunder.nutrition.shop@gmail.com'