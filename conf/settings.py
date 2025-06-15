from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ln1jd=+kjs@r&hzw!oaubjlf)w25&+kn5h7$g=5g@s#3xwav5#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # my apps
    'base',
    'blog',
    'coffee',

    # 'djrichtextfield',
    'ckeditor',         # <--- Bu qatorni qo'shing
    'ckeditor_uploader',
]



# myproject/settings.py

# ... boshqa sozlamalar

# CKEditor sozlamalari
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full', # Yoki 'Basic', 'Standard' yoki o'zingiz xohlagan tugmalar ro'yxati
        'height': 300,
        'width': 800,
        'extraPlugins': 'codesnippet', # Agar kod snippetlarini qo'shmoqchi bo'lsangiz
        'skin': 'moono', # CKEditor skin (moono, kama, office2003)
        # 'uiColor': '#9AB8F3', # Rang berish
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Source', '-', 'Maximize'],
            ['CodeSnippet'], # Yuqoridagi extraPlugins ichida bo'lsa
        ],
        'filebrowserBrowseUrl': '/ckeditor/browse/', # Rasmlar/fayllar brauzeri URL
        'filebrowserUploadUrl': '/ckeditor/upload/', # Rasmlar/fayllar yuklash URL
    },
    # Agar boshqa turdagi CKEditorga ega bo'lishni xohlasangiz, bu yerga qo'shishingiz mumkin
    'simple': {
        'toolbar': 'Basic',
        'height': 200,
        'width': 600,
    },
}

# CKEditor yuklash yo'li sozlamasi
CKEDITOR_UPLOAD_PATH = 'uploads/' # Media papkasida 'uploads' papkasi ichiga rasmlar yuklanadi



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processor.index_processor',
                'coffee.context_processor.index_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


STATIC_URL = '/static/'#Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')


# Base url to serve media files
MEDIA_URL = '/media/'
# Path where media is stored'
MEDIA_ROOT = BASE_DIR / 'media'
# Older versions of Django that use os module for path traversal do this instead
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
