# To make our modular code into package

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="AI Travel Planner Agent",
    version="0.2",
    author= "Mitesh Upadhyay",
    packages=find_packages(),
    install_requires=requirements
)