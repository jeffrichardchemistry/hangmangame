# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='hangmangame',
    version='0.0.1',
    url='https://github.com/jeffrichardchemistry/hangmangame',
    license='GNU General Public License v3.0',
    author='Jefferson Richard',
    author_email='jrichardquimica@gmail.com',
    keywords='Game terminal hangman',
    description='Hangman game for terminal',
	long_description = description,
	long_description_content_type = "text/markdown",
    packages=['hangmangame'],
    install_requires=['numpy'],
	classifiers = [
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3']
)
