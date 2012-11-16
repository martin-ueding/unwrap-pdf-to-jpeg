#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from distutils.core import setup

setup(
    author = "Martin Ueding",
    author_email = "dev@martin-ueding.de",
    description = "Converts JPEG files to PDF and back",
    license = "GPL2+",
    name = "wrap-jpeg-to-pdf",
    scripts = ["wrap-jpeg-to-pdf", "unwrap-pdf-to-jpeg"],
    version = "1.0",
)