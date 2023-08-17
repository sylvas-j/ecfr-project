from .common import *
###############
## configuration for heroku
# import dj_database_url
# import django_heroku
####################

DEBUG = True

ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:8383',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8383',
    'http://www.devarchive.org:8383',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://localhost:8383',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8383',
    'http://www.devarchive.org:8383',
]

# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': os.environ.get('MYSQL_ENGINE'),
#         'NAME': os.environ.get('MYSQL_DATABASE'),
#         'USER': os.environ.get('MYSQL_USER'),
#         'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
#         'HOST': os.environ.get('MYSQL_HOST'),
#         'PORT': os.environ.get('MYSQL_PORT'),
#         'OPTIONS': {
#             'auth_plugin': 'mysql_native_password'
#         }

#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)