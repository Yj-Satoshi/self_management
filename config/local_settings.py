import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'management',
        'USER': 'root',
        'PASSWORE': '',
    }
}
ALLOWED_HOSTS = []
DEBUG = True
