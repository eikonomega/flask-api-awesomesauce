"""
Flask-Api-Awesomesauce
-------------
See README.md

"""
from setuptools import setup, find_packages
import flask_api_awesomesauce


setup(
    name='Flask-Api-Awesomesauce',
    version=flask_api_awesomesauce.__version__,
    url='https://github.com/eikonomega/flask-api-awesomesauce',
    license='MIT',
    author='Mike Dunn',
    author_email='mike@eikonomega.com',
    description='Flask Api Awesomesauce!',
    long_description=flask_api_awesomesauce.__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'PyTest',
        'pytest-cov'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

