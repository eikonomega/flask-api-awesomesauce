"""
Flask-Api-Panda
-------------
See README.md

"""
from setuptools import setup, find_packages
import flask_api_panda


setup(
    name='Flask-Api-Panda',
    version=flask_api_panda.__version__,
    url='https://github.com/eikonomega/flask-api-panda',
    license='MIT',
    author='Mike Dunn',
    author_email='mike@eikonomega.com',
    description='Flask Ape Awesomesauce for Pandas!',
    long_description=flask_api_panda.__doc__,
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

