from setuptools import setup, find_packages

setup(
    name="redknot-data-pipeline",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.35",
        "requests>=2.32",
        "pandas>=2.2",
    ],
)
