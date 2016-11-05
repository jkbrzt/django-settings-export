SECRET_KEY = 'spam'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'demo.urls'
INSTALLED_APPS = ['demo']

# TEMPLATES is used by Django >= 1.8. TEMPLATE_CONTEXT_PROCESSORS below is for compatibility with older versions.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django_settings_export.settings_export',
            ],
        },
    },
]
TEMPLATE_CONTEXT_PROCESSORS = ['django_settings_export.settings_export']

DATABASES = {'default': {'NAME': 'db.sqlite',
                         'ENGINE': 'django.db.backends.sqlite3'}}


FOO = 'foo'
BAR = 'bar'
SETTINGS_EXPORT = [
    'FOO',
    'BAR',
]
