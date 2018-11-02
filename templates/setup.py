#!/usr/bin/env python3

from setuptools import setup

setup(name='<%!package_name!%>',
      version='<%!version!%>',
      description='<%!description!%>',
      author='<%!author!%>',
      author_email='<%!email!%>',
      install_requires=[
          <%!install_requires!%>
      ],
      url='<%!git_url!%>',
      packages=['<%!package_name!%>'],
      entry_points = {
              'console_scripts': [
                  <%!console_scripts!%>
              ],
          },
     )
