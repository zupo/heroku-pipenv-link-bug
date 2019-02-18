"""Installer for the pipenvbug package."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='pipenvbug',
    version='0.1',
    description='Pyramid based app for showcasing a pipenv bug at '
                'https://github.com/heroku/heroku-buildpack-python/issues/687',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: Other/Proprietary License',
    ],
    author='Niteo',
    author_email='info@niteo.co',
    url='http://github.com/zupo/heroku-pipenv-link-bug',
    keywords='pyramid pipenvbug',
    license='Proprietary',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points="""\
    [paste.app_factory]
    main = pipenvbug:main
    """,
    test_suite='pipenvbug',
)
