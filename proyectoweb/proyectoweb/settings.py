from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8%5q81i+9qyl)@j)!10cknx821x*7sm%c2d_=_y1^kn&s)uepo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

STATICFILES_DIRS= ['C:/Proyecto/proyectoweb/proyectowebapp/static']

#Configuraremos los mensajes de error del proyecto
from django.contrib.messages import constants as mensajes_de_error

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectowebapp',
    'servicios',
    'blog',
    'tienda',
    'carro',
    'autenticacion',
    'crispy_forms',
    'crispy_bootstrap5',
    'pedidos',
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

ROOT_URLCONF = 'proyectoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['C:/Proyecto/proyectoweb/proyectoweb/template/proyectowebapp', 'C:/Proyecto/proyectoweb/tienda/template/tienda', 'C:/Proyecto/proyectoweb/tienda/template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'proyecto1',
        'USER': 'admin_store',
        'PASSWORD':'',
        'HOST':'localhost',
        'POST':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

#las siguientes carpetas permiten cargar los archivos de imagen

MEDIA_URL='/media/'
MEDIA_ROOT='C:/Proyecto/proyectoweb/blog/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webstorewarriors@gmail.com'
EMAIL_HOST_PASSWORD = 'h g a l s l d g s j s o k a q i' #Constraseña de la aplicación

#Permite configurar la aplicación crispy para formularios

CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

#Etiquetas de mensajes
MESSAGES_TAGS = {
    mensajes_de_error.DEBUG:'debug',
    mensajes_de_error.INFO:'info',
    mensajes_de_error.WARNING:'info',    
    mensajes_de_error.SUCCESS:'success',
    mensajes_de_error.ERROR:'danger',
}