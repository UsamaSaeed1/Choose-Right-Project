"""
Django settings for chooseright project.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^zq)jnd@b07pjy5*(j5gif9g_rs3o@!)@807^!!=#bfknp7trd'
#SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    #Aullauth apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    #My Apps

    'core',
    'users',

    #Libraries
    'crispy_forms',
    'tellme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chooseright.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'chooseright.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chooseright_database',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}


# Password validations
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

#Registration with Confirmation Mail
# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = 'Choose Right Team <admin@chooseright.com>'


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# For deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


#Handling static files uploaded by user
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Authentication Setting
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    # Bbackend authentication by email or username
    'users.backends.EmailBackend'
]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#Redirect Users to profile page after successfull login
LOGIN_REDIRECT_URL = 'users:dash_board'

#Redirect Users to login page before accessing restricted content
LOGIN_URL = 'users:login'

#Redirect Users to homepage after successfull logout
LOGOUT_REDIRECT_URL = '/'

#Close user session when site tab is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#Send email to admin whenever user provides feedback
TELLME_FEEDBACK_EMAIL = os.environ.get('EMAIL_USER')
