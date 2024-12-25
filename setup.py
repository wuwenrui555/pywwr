from setuptools import setup, find_packages

setup(
    name="pywwr",
    version="0.0.1",
    description="Random Python utilities for Wenrui",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="wuwenrui555",
    author_email="wuwenruiwwr@outlook.com",
    url="https://github.com/wuwenrui555/pywwr",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
