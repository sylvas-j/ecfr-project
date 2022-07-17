"""
ASGI config for ecfr_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from helpers.credentials import dev_prod

dev_prod()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecfr_project.settings')

application = get_asgi_application()
