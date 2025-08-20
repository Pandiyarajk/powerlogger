#!/usr/bin/env python3
"""
Setup script for PowerLogger package.
"""

import os

from setuptools import find_packages, setup


def read_readme():
    """Read README.md file."""
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "PowerLogger - Enhanced logging functionality with Rich console output and file rotation."


def read_requirements():
    """Read requirements.txt file."""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [
                line.strip() for line in fh if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        return []


setup(
    name="powerlogger",
    version="0.1.0",
    author="Pandiyaraj Karuppasamy",
    author_email="pandiyarajk@live.com",
    description="Enhanced logging functionality with Rich console output and file rotation",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pandiyarajk/powerlogger",
    project_urls={
        "Bug Tracker": "https://github.com/Pandiyarajk/powerlogger/issues",
        "Changelog": "https://github.com/Pandiyarajk/powerlogger/blob/main/CHANGELOG.md",
        "Documentation": "https://github.com/Pandiyarajk/powerlogger/blob/main/README.md",
        "Repository": "https://github.com/Pandiyarajk/powerlogger",
        "Source Code": "https://github.com/Pandiyarajk/powerlogger",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
    python_requires=">=3.11",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "build>=0.10.0",
            "twine>=4.0.0",
        ],
    },
    package_data={
        "powerlogger": ["*.ini", "*.txt"],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="logging, rich, console, utf8, unicode, thread-safe, file-rotation, windows",
)
