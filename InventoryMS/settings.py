
import os
from pathlib import Path
import dj_database_url#-
import dj_database_url#+
#+
BASE_DIR = Path(__file__).resolve().parent.parent#+
#+
DATABASES = {#+
    'default': dj_database_url.config(#+
        default=f'sqlite:///{BASE_DIR}/db.sqlite3'#+
    )#+
}#+


DATABASES['default'] = dj_database_url.config(default=f'sqlite:///{BASE_DIR}/db.sqlite3')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g_n2+2bznu6e@1wel!i(&-4tp86_7lop5395ww+i4x%9*7^old'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False in production

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'pos-b63z.onrender.com',  # Add your Render domain
]

CSRF_TRUSTED_ORIGINS = [
    'https://pos-b63z.onrender.com',  # Render domain
]
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'phonenumber_field',
    'crispy_forms',
    'crispy_bootstrap5',
    'imagekit',
    'django_extensions',
    'django_filters',
    'django_tables2',

    'store.apps.StoreConfig',
    'accounts.apps.AccountsConfig',
    'transactions.apps.TransactionsConfig',
    'invoice.apps.InvoiceConfig',
    'bills.apps.BillsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add WhiteNoise remove letter
]

ROOT_URLCONF = 'InventoryMS.urls'

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

WSGI_APPLICATION = 'InventoryMS.wsgi.application'

# Database Configuration (SQLite for development, switch to PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LOGIN_URL = 'user-login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_URL = 'logout'

# Static and Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'static/images'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Add this line
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms Configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
