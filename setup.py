# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='template_pac',
    version='0.0.1',
    description='template package',
    long_description=readme,
    author='Tsuyoshi Ishizone',
    author_email='tsuyoshi.ishizone@gmail.com',
    install_requires=['numpy'],
    python_requires=">=3",
    license=license,
    url='https://github.com/ZoneTsuyoshi/template-pac',
    packages=find_packages(include='template_pac'),
    py_modules=["math"],
    test_suite='tests'
)

