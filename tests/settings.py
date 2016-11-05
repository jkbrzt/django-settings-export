SECRET_KEY = 'spam'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'tests.urls'
INSTALLED_APPS = ['tests']
DATABASES = {'default': {'NAME': 'db.sqlite',
                         'ENGINE': 'django.db.backends.sqlite3'}}

# Django < 1.8
TEMPLATE_CONTEXT_PROCESSORS = [
    'django_settings_export.settings_export'
]
# Django 1.8+
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


FOO = 'foo'
BAR = 'bar'
SETTINGS_EXPORT = [
    'FOO',
    'BAR',
]
