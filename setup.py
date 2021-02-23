from setuptools import setup, find_packages
import sys
from typing import List

install_requires: List[str] = [
    'peewee >= 3.14.1',
    'peewee_migrate >= 1.4.0',
    'passlib >= 1.7.4',
    'email_validator >= 1.1.2',
    'fastapi >= 0.63.0',
    'pydantic >= 1.7.3',
]

setup(
    name='fastauth',
    version='0.1.0-alpha',

    packages=find_packages(exclude=[ 'tests', ]),
    install_requires=install_requires,

    author='aoirint',
    author_email='aoirint@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
