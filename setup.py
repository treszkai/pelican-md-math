#!/usr/bin/env python

from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="pelican-convert-math",
    version="0.0.0",
    author="Laszlo Treszkai",
    author_email="laszlo.treszkai@gmail.com",
    packages=find_packages(),
    url="https://github.com/treszkai/convert-math",
    license="AGPL-3.0",
    description="Convert math tags in markdown input for Pelican",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=["pelican>=4.5"],
    include_package_data=True,  # includes files from MANIFEST.in
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pelican :: Plugins",
        "Framework :: Pelican",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
    ],
)
