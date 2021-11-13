from setuptools import setup
from constants import ALIAS

setup(
  name='todo-ksumit',
  author='Sumit kushwah',
  url='https://github.com/sumit-kushwah/todo-cli',
  description="""
  This project provides simple task manager tool for developers in terminal.
  There are multiple commands supported. For docs and code please visit homepage url.
  """,
  version='0.0.1',
  py_modules=['todo-ksumit'],
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