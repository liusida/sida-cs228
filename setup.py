from setuptools import find_packages, setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='sida_cs228',
    version='0.0.2',
    packages=find_packages('.'),
    py_modules=["sida"],
    install_requires=[
            'numpy',
            'matplotlib'
        ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/liusida/sida-cs228/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sida Liu",
    author_email="sliu1@uvm.edu",

)