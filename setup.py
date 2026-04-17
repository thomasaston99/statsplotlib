# setup.py
from setuptools import setup, find_packages

setup(
    name="statsplotlib",
    version="0.1.0",
    description="STATSports plotting utilities and branding for matplotlib plots.",
    author="Thomas Aston",
    packages=find_packages(),
    include_package_data=True, # include non-Python files like fonts/logos
    install_requires=[
        "matplotlib>=3.5.0"
    ],
)