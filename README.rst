.. Copyright © 2012-2014, 2016-2017 Martin Ueding <dev@martin-ueding.de>

##################
unwrap-pdf-to-jpeg
##################

.. note::

    Although this worked for me for a while, I reverted to standard PDF files.
    The workflow is much easier and other people can work with PDF files
    directly as opposed to a folder full of JPEG files.

    There still is the ``wrap-jpegs-to-pdf`` command in this project, which is
    just a wrapper for ``convert``. Feel free to just use that like so::

        $ convert images-*.jpg scanned.pdf

A lot of my documents are scanned, and I used to save them as JPEG files and
then combine them into a single PDF for better handling.

The downside is that I cannot do anything with the original JPEG images any
more, and I did not keep those. Luckily, there is a nice tool called
``pdfimages``.

Since I like my files to be numbered with an ``+1``, ``+2``, and so forth, I
wrote a script that unwraps the image files from the PDF and numbers them for
me.

That way, I can directly use it together with my *multiimage* tool.
