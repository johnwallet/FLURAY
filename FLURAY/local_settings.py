from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = '_q6_93ep53#%a*nar65cgzo=gnmd49wbvnywhp)ry5b^772=4n'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fluray',
        'USER': 'admin',
        'PASSWORD': 'Ghjkl5678',
        'HOST': 'Localhost',
        'PORT': 5432,
    }
}

# smtp
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = '587'
EMAIL_HOST_USER = "aleksandrvarlamov1753@gmail.com"
EMAIL_HOST_PASSWORD = "Tesla007"

RECAPTCHA_PUBLIC_KEY = "6Lc_al8aAAAAAMDGV3hW5A24uwboL5GMvdGQJcjM"
RECAPTCHA_PRIVATE_KEY = "6Lc_al8aAAAAAOKdC6pJGVP2s16mcq-6Qo4kpr3b"
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5


