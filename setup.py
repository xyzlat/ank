__author__ = 'sunary'


import os
from setuptools import setup, find_packages
from utils import VERSION


def __path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

with open('LICENSE') as fo:
    license = fo.read()

reqs = ['psutil==3.3.0', 'kombu==3.0.33', 'pymongo==3.2', 'amqp==1.4.9', 'pyyaml==3.11',
        'redis==2.10.5', 'flask==0.11', 'gevent==1.1.1']

setup(
    name='ANK',
    version=VERSION,
    author='Sunary [Nhat Vo Van]',
    author_email='v2nhat@gmail.com',
    maintainer='Sunary [Nhat Vo Van]',
    maintainer_email='v2nhat@gmail.com',
    description='Python Microservices',
    long_description='ANK - Microservices.\nSee at: https://github.com/sunary/ank',
    license=license,
    keywords='ank, microservice, rabbitMQ, kafka, zeroMQ, queue, stream',
    url='https://github.com/sunary/ank',
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=reqs,
    entry_points={
        'console_scripts': ['ank = PYTHONPATH=$(pwd) python cmd.py']
    },
)