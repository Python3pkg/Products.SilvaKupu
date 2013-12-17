# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from setuptools import setup, find_packages
import os

version = '1.4.3dev'

setup(name='Products.SilvaKupu',
      version=version,
      description="Kupu WYSIWYG text editor for Silva.",
      long_description=open(os.path.join("Products", "kupu", "doc", "README.txt")).read() + "\n" +
                       open(os.path.join("Products", "kupu", "doc", "CHANGES.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Editors",
        ],
      keywords='kupu silva zope2',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/products/kupu_editor',
      license='Kupu License',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
