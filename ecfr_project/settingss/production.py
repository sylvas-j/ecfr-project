from .common import *
###############
## configuration for heroku
import dj_database_url
import django_heroku
####################

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','https://ecfr-rsu.herokuapp.com/']


# TEST/DEVELOPMENT REMOTE DATABASE
DATABASES = {
    # 'default': {},
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db4free.net',
        'PORT': '3306',
        'NAME': 'sn_rsu_db',
        'USER': 'sn_test_user',
        'PASSWORD': 'sn_test_user',
    },
}




django_heroku.settings(locals())
django_heroku.settings(config=locals(), staticfiles=False,logging=False)

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

# # settings.py
# AUTHENTICATION_BACKENDS = (
#     'admin_panels.backends.EmailBackend',
#     )

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# configuration for heroku
##################
ADMINS = (('Webmaster','sylvanusjerome@gmail.com'))
MANAGERS = ADMINS


EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ba7606b4e3166d'
EMAIL_HOST_PASSWORD = 'd561301a16f63b'
EMAIL_PORT = '2525'
# 465

