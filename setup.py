from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='mezzanine_facebook',
    version='0.2',
    description='Facebook app for Django Mezzanine CMS',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='django mezzanine cms facebook',
    author='Sasha Vladimirskiy',
    author_email='sasha@butchershop.co',
    url='http://www.butchershop.co/',
    license='bsd',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Mezzanine==4.2.0',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
