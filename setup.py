#!/usr/bin/env python3

from setuptools import setup

setup(name='pymk_package',
      version='1.0.0',
      description='',
      author='Lee Thompson',
      author_email='',
      install_requires=[],
      url='',
      packages=['pymk_package'],
      entry_points = {
              'console_scripts': [
                  'pymk_package = pymk_package.pymk_package:cl_mk_package',
              ],
          },
     )
