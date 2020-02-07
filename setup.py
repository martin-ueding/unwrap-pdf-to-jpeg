#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Martin Ueding <martin-ueding.de>

from distutils.core import setup

setup(
    author = "Martin Ueding",
    description = "Converts JPEG files to PDF and back",
    license = "GPL2+",
    name = "wrap-jpeg-to-pdf",
    scripts = [
        "move-pdf-source",
        "unwrap-pdf-to-jpeg",
        "wrap-jpeg-to-pdf",
        "wrap-tar",
    ],
    version = "1.0",
)
