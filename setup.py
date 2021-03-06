import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='yak-server',
    version='0.1',
    packages=['yak'],
    install_requires=[
        'Django>=1.7',
        'djangorestframework>=3.0.0, !=3.0.1',
        'Pillow>=2.5',
        'django-filter>=0.7',
        'django-model-utils>=2.0',
        'django-oauth-toolkit>=0.7.2',
        'facebook-sdk==0.4.0',
        'factory-boy>=2.4',
        'mock>=1.0',
        'python-instagram>=1.3.0',
        'python-memcached>=1.53',
        'python-social-auth>=0.2',
        'python-swiftclient>=2.2',
        'requests>=2.1',
        'requests-oauthlib>=0.4',
        'twython>=3.1'
    ],
    dependency_links=[
        "git+ssh://git@github.com/jbalogh/django-cache-machine.git#egg=django_cache_machine-master"
    ],
    include_package_data=True,
    license='BSD License',
    description='Server-side implementation of Yeti App Kit built on Django',
    long_description=README,
    url='https://yeti.co/yeti-app-kit/',
    author='Baylee Feore',
    author_email='baylee@yeti.co',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
