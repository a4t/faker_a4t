from setuptools import setup, find_packages
import sys

sys.path.append('./faker_a4t')

setup(name='faker_a4t',
      version='0.0.1',
      description='Faker test',
      author='a4t',
      author_email='iwanomoto@gmail.com',
      url='https://github.com/a4t/faker_a4t',
      packages=find_packages(exclude=('tests')),
      test_suite='tests')
