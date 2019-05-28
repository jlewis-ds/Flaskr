# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:51:17 2019

@author: jlewis
"""

from setuptools import find_packages, setup

setup(
      name='flaskr',
      version='1.0.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
              'flask',
              ],
)