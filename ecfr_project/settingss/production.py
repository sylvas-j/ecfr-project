from .common import *
###############
## configuration for heroku
# import dj_database_url
# import django_heroku
####################

DEBUG = True

ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8383',
    'http://devarchive.org',
    'https://devarchive.org',
    'http://www.devarchive.org',
    'https://www.devarchive.org',
    'http://devarchive.org:8383',
    'http://www.devarchive.org:8383',
]

CORS_ORIGIN_WHITELIST = [
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

# django_heroku.settings(locals())
# django_heroku.settings(config=locals(), staticfiles=False,logging=False)

# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

# # settings.py
# AUTHENTICATION_BACKENDS = (
#     'admin_panels.backends.EmailBackend',
#     )

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# configuration for heroku
##################
# ADMINS = (('Webmaster','sylvanusjerome@gmail.com'))
# MANAGERS = ADMINS


EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ba7606b4e3166d'
EMAIL_HOST_PASSWORD = 'd561301a16f63b'
EMAIL_PORT = '2525'
# 465

