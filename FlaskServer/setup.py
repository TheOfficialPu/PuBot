"""setup file for the FlaskServer package
"""
import unittest
from setuptools import setup, find_packages

def readme():
    """returns the text of the readme.md file
    """
    with open('README.md') as readme_file:
        return readme_file.read()


def package_test_suite():
    """load the test suit
    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    return test_suite

setup(name='flaskserver',
      version='v0.1.0',
      description=('This package is a flask server build to host the thing'),
      long_description=readme(),
      url='https://github.com/TheOfficialPu/PuBot',
      author='Apurv Prashanth',
      author_email='a2prasha@uwaterloo.ca',
      license=None,
      packages=find_packages(),
      install_requires=["sqlalchemy", "flask", "flask-bcrypt", "flask-login",
                        "Flask-SQLAlchemy", "Flask-Testing", "Flask-WTF"],
      dependency_links=[],
      include_package_data=True,
      test_suite='setup.package_test_suite',
      zip_safe=False)
