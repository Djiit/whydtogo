from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Whyd To Go',
    version='0.1.1',
    description='Whyd To Go - Take your Whyd playlists away',
    long_description=long_description,
    url='https://github.com/Djiit/whydtogo',
    author='Julien Tanay',
    author_email='julien.tanay@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='whyd scraping youtube-dl',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['peppercorn'],
    entry_points={
        'console_scripts': [
            'whydtogo=whydtogo:main',
        ],
    },
)
