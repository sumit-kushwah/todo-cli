from setuptools import setup

setup(
  name='todo',
  version='0.0.1',
  py_modules=['todo'],
  install_requires=[
    'Click'
  ],
  entry_points={
    'console_scripts': [
      'todo = cli:cli',
    ]
  }
)