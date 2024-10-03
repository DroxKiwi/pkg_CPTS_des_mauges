from setuptools import setup, find_packages
import bdd
import os

# (pip install setuptools)
# (pip install wheel)
# python setup.py bdist_wheel
# python setup.py install
# pip wheel -r requirements.txt
# python setup.py sdist --formats=gztar,zip
# python setup.py sdist

setup(name='CPTSdal',
      version='1.0.0',
      author='Corentin Fredj',
      author_email='corentinfredj.dev@gmail.fr',
      maintainer='Salesky',
      maintainer_email='corentinfredj.dev@gmail.fr',
      keywords='KDDS Development',
      classifiers=['Topic :: Pro', 'Topic :: Base'],
      packages=['bdd', 'bdd.dbcpts'],
      include_package_data=True,
      description='Package CPTS DAL',
      long_description=open(os.path.join(
          os.path.dirname(__file__), 'README.md')).read(),
      license='GPL V3',
      platforms='ALL',
      install_requires=['psycopg>=2.9.9',
                        'SQLAlchemy==1.4.23'])