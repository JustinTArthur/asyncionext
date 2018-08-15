# -*- coding: utf-8 -*-
# Copyright © 2018 Justin Turner Arthur
from setuptools import setup, find_packages

setup(
    name='asyncionext',
    version='0.1.0',
    description='A collection of features proposed for the asyncio standard '
                'library for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=('aiofiles<0.5.0>=0.4.0'),
    classifiers=(
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    keywords=('asyncio', 'files'),
    author='Justin Turner Arthur and contributors',
    author_email='justinarthur@gmail.com',
    url='https://github.com/JustinTArthur/asyncionext',
    packages=find_packages(exclude=('tests', 'examples')),
)
