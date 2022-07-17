import os
from django.core.wsgi import get_wsgi_application
from helpers.credentials import dev_prod

dev_prod()

application = get_wsgi_application()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecfr_project.settings')

# configuration for heroku
######################
from whitenoise import WhiteNoise
# from whitenoise.django import DjangoWhiteNoise
application = WhiteNoise(application)
#######################

