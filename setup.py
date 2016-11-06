import codecs
from setuptools import setup

try:
    import multiprocessing
except ImportError:
    pass


with codecs.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()


setup(
    name="django-settings-export",
    version='1.2.1',
    author="Jakub Roztocil",
    author_email="jakub@roztocil.co",
    description='This Django app allows you to export'
                ' certain settings to your templates.',
    long_description=long_description,
    license='BSD',
    url='https://github.com/jkbrzt/django-settings-export',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['django_settings_export'],
    install_requires=['django'],
)
