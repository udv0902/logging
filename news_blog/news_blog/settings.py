"""
Django settings for news_blog project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@ps!ndq-vu=@qdn%4nt08j_i((nx%nf7mn*gsoko_i2+e8h4_!'

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
    'news.apps.NewsConfig',
    'accounts.apps.AccountsConfig',
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

ROOT_URLCONF = 'news_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'news_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_debug_format': {
            'format': '{asctime} {levelname}  - {message}',
            'style': '{',
        },
        'console_warning_format': {
            'format': '{asctime} {levelname}  - {message} - {pathname}',
            'style': '{',
        },
        'console_error_critical_format': {
            'format': '{asctime} {levelname}  - {message} - {pathname} - {exc_info}',
            'style': '{',
        },
        'mail_format': {
            'format': '{asctime} {levelname}  - {message} - {pathname}',
            'style': '{',
        },
        'security_format': {
            'format': '{asctime} {levelname}  - {module} - {message}',
            'style': '{',
        },
        'general_log_format': {
            'format': '{asctime} {levelname} - {module} - {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'console_debug_format',
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning_format',
        },
        'console_error_critical': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'console_error_critical_format',
        },
        'general_file': {
            'class': "logging.FileHandler",
            'filename': "general.log",
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'formatter': 'general_log_format',
        },
        'errors_file': {
            'class': "logging.FileHandler",
            'filename': "errors.log",
            'level': "ERROR",
            'formatter': 'console_error_critical_format',
        },
        'security_file': {
            'class': "logging.FileHandler",
            'filename': "security.log",
            'level': "WARNING",
            'formatter': 'security_format',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'mail_format',
        },
    },
    'loggers': {
        'django': {
            'console_debug': {
                'handlers': ['console'],
                'propagate': True,
            },
        },
        'console_warning': {
            'handlers': ['console_warning'],
            'propagate': True,
        },
        'console_error': {
            'handlers': ['console_error_critical'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'logfile': {
#             'class': 'logging.FileHandler',
#             'filename': 'server.log',
#         },
#         'console': {
#             'class': 'logging.StreamHandler'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'logfile'],
#         },
#     },
# }
