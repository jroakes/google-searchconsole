# encoding: utf-8

from setuptools import find_packages, setup


setup(name='searchconsole',
      description='A wrapper for the Google Search Console API.',
      author='Josh Carty',
      author_email='carty.josh@gmail.com',
      version='0.0.3',
      license='MIT',
      packages=find_packages(),
      keywords='data analysis search console google api seo',
      install_requires=[
          'google-api-python-client',
          'python-dateutil',
          'google-auth',
          'google-auth-oauthlib'
      ],
      test_suite='tests'
      )
