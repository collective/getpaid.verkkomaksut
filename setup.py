from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('getpaid', 'verkkomaksut', 'version.txt')[:-1]

long_description = (
                        open(os.path.join("docs", "HISTORY.txt")).read() + "\n" +
                        open(os.path.join("docs", "INSTALL.txt")).read()
    )

setup(name='getpaid.verkkomaksut',
      version=version,
      description="Verkkomaksut payment processor for getpaid.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Taito Horiuchi',
      author_email='taito.horiuchi@gmail.com',
      url='http://pypi.python.org/pypi/getpaid.verkkomaksut',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['getpaid'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
#          'getpaid.recipe.release'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
