"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import django
from pathlib import Path
from django.utils.encoding import smart_str

django.utils.encoding.smart_text = smart_str
USE_SQLITE = os.environ.get("USE_SQLITE", default=False)
if USE_SQLITE=="True":
    USE_SQLITE=True
print("Use sqlite: ", USE_SQLITE)
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
print("Database port: ", DATABASE_PORT, "Database host: ", DATABASE_HOST)
COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default="")
# COGNITO_USER_POOL = os.environ.get('COGNITO_USER_POOL', default="")
COGNITO_AWS_REGION = os.environ.get("COGNITO_AWS_REGION", default="")
COGNITO_USER_POOL_NAME = os.environ.get("COGNITO_USER_POOL_NAME", default="")
COGNITO_CLIENT_ID = os.environ.get("COGNITO_CLIENT_ID", default="")
COGNITO_CLIENT_SECRET = os.environ.get("COGNITO_CLIENT_SECRET", default="")
SOCIALACCOUNT_STORE_TOKENS = True
SOCIALACCOUNT_PROVIDERS = {
    "amazon_cognito": {
        "DOMAIN": f"https://{COGNITO_USER_POOL_NAME}.auth.{COGNITO_AWS_REGION}.amazoncognito.com",
        "APP": {
            "client_id": f"{COGNITO_CLIENT_ID}",
            "client_secret": f"{COGNITO_CLIENT_SECRET}",
            "secret": "",
            "key": "",
        },
    },
}
ACCOUNT_EMAIL_VERIFICATION = "none"
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qb!j$aqlb)haze)!#1=p!!j1*q4@)rc#zk&!(v*+))(=)lli2l"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("http://localhost:8000",)
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "kb.apps.kb_appConfig",
    "corsheaders",
    "data",
    "people_depot.apps.pd_appConfig",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # include the providers you want to enable:
    "allauth.socialaccount.providers.amazon_cognito",
    "rest_framework",
    "drf_spectacular",
    # autocomplete light
    "dal",
    "dal_select2",
    'queryset_sequence',
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # Other DRF settings...
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # CORS
    "django.middleware.common.CommonMiddleware",
    # people depot config
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databasescr
AUTH_USER_MODEL = "people_depot.User"
LOGIN_REDIRECT_URL = "/admin/"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
        },
    },
    "loggers": {
        "mylogger": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}
if not USE_SQLITE:
    print("Using postgres")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
        }
    }
else:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / "db.sqlite3",
            }
        }

# ƒ validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
