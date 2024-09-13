"""
Django settings for ResumeCraft project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    "debug_toolbar",
    "rest_framework",
    "jalali_date",
    'django_jalali',
    # Local apps
    'dashboard',
    "accounts",
    'resume',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'accounts.middleware.SessionExpiredMiddleware',
]

ROOT_URLCONF = 'ResumeCraft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ResumeCraft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'pgdb'),  # Adjust as per your docker-compose service name
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Jalali Date defaults
JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            'admin/js/django_jalali.min.js',
            'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

LANGUAGES = [ ('fa', _('Persian'))]

LANGUAGE_CODE = 'fa-ir'
USE_I18N = True
TIME_ZONE = 'Asia/Tehran'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/app/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Accounts (Custom User Model)
SITE_ID = 1
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'dashboard'
AUTH_USER_MODEL = 'accounts.CustomUser'
SESSION_COOKIE_AGE = (60 * 60 * 4)  # 240 minutes in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
LOGIN_URL = '/app/accounts/login/'

# Email settings
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'False') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@example.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-password')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-default")
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# SSL & Security settings
SECURE_SSL_REDIRECT = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "False") == "True"
SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", "False") == "True"
SECURE_HSTS_PRELOAD = os.environ.get("DJANGO_SECURE_HSTS_PRELOAD", "False") == "True"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Secure Cookies
SESSION_COOKIE_SECURE = os.environ.get("DJANGO_SESSION_COOKIE_SECURE", "False") == "True"
CSRF_COOKIE_SECURE = os.environ.get("DJANGO_CSRF_COOKIE_SECURE", "False") == "True"

# Message Storage
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Debug Toolbar
INTERNAL_IPS = ["127.0.0.1",]

# Cache Configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL', 'redis://:6x9HiF2TGgNj7bYATaR@redis:6379/1'),
    }
}

# Celery configuration
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://:6x9HiF2TGgNj7bYATaR@redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", CELERY_BROKER_URL)

# MIME Types Fixes
import mimetypes
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)