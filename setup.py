from setuptools import setup, find_packages

version = '1.1'

setup(name='pyzipcode',
      version=version,
      description="query zip codes and location data",
      long_description=open("README.txt").read() + '\n\n' + open('CHANGES.txt').read(),
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='zip code distance',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'pysqlite'
      ],
      python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
