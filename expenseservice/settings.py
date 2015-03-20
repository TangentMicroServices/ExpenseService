"""
Django settings for hoursservice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*_ac&t31acs3_)@+636p(xuu!9i&n5)tw#y)5a2xjfajiwubk5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## 3rd party
    'rest_framework',
    'rest_framework_swagger',

    ## custom
    'tokenauth',
    'api',

    # testing etc:
    'django_jenkins',
    'django_extensions',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'tokenauth.middleware.TokenAuthMiddleware',

)

ROOT_URLCONF = 'expenseservice.urls'

WSGI_APPLICATION = 'expenseservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True

###
# App Specific configurations
###

# CUSTOM AUTH
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tokenauth.authbackends.TokenAuthBackend'
)

## REST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'tokenauth.authbackends.RESTTokenAuthBackend',        
    )
}

# Services:


JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    # 'django_jenkins.tasks.run_sloccount',
    # 'django_jenkins.tasks.run_graphmodels'
)

PROJECT_APPS = (
    'api',
)

SWAGGER_SETTINGS = {
    'api_key': 'fb5df470df0fa3727c49a61608996618d0954289',
    'info': {
        'contact': 'admin@tangentsolutions.co.za',
        'description': '...',
        'license': 'MIT',
        'title': 'ExpenseService',
    },

}

STATIC_ROOT = '/srv/static/expenseservice/static/'

## Service base urls without a trailing slash:
USERSERVICE_BASE_URL = 'http://staging.userservice.tangentme.com'
PROJECTSERVICE_BASE_URL = "http://staging.projectservice.tangentme.com"