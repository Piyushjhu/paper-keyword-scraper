#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="paper-keyword-scraper",
    version="2.0.0",
    author="Piyush Wanchoo",
    author_email="piyushwanchoo@gmail.com",
    description="A legitimate tool for analyzing academic keyword trends using the Semantic Scholar API",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Piyushjhu/paper-keyword-scraper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "paper-keyword-scraper=academic_keyword_analyzer:main",
        ],
    },
    keywords="academic research keyword analysis semantic scholar api trends visualization",
    project_urls={
        "Bug Reports": "https://github.com/Piyushjhu/paper-keyword-scraper/issues",
        "Source": "https://github.com/Piyushjhu/paper-keyword-scraper",
        "Documentation": "https://github.com/Piyushjhu/paper-keyword-scraper#readme",
    },
    include_package_data=True,
    zip_safe=False,
) 