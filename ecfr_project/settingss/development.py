from .common import *

DEBUG = True
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['127.0.0.1','localhost','https://ecfr-madonna.herokuapp.com/']


DATABASE_ROUTERS = ['routers.db_routers.EcfrRouter',
                    # 'routers.db_routers.AuthRouter',
                    ]

#TEST/DEVELOPMENT LOCAL DATABASE
DATABASES = {
    'default': {},
    'ecfr_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecfr_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}



# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'ba7606b4e3166d'
EMAIL_HOST_PASSWORD = 'd561301a16f63b'
EMAIL_PORT = '2525'
# 465
