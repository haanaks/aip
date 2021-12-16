from setuptools import setup

with open('README.md') as file:
    read_me_description = file.read()

setup(
    name='Practice',
    version='1.0',
    author='User',
    packages=['src'],
    python_requires='>=3.5',
)
