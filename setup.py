from setuptools import setup, find_packages

version = __import__('insertblocks').__version__

setup(
    name = 'django-sekizai',
    version = version,
    description = 'Django Sekizai',
    author = 'Jonas Obrist',
    author_email = 'jonas.obrist@divio.ch',
    url = 'http://github.com/ojii/django-sekizai',
    packages = find_packages(),
    zip_safe=False,
)