from setuptools import setup
from constants import ALIAS

setup(
  name='todo',
  version='0.0.1',
  py_modules=['todo'],
  install_requires=[
    'Click',
    'tabulate'
  ],
  entry_points={
    'console_scripts': [
      f'{ALIAS} = cli:cli',
    ]
  }
)