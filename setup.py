from setuptools import find_packages, setup

setup(
    name='basicapi',
    version='1.0.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
