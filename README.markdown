# unwrap PDF into JPEG files

This converts a PDF file into the JPEG files it was made out of initially and numbers them with a `+1`, `+2`, ... scheme.

Basically, it is just a simple wrapper for `pdfimages -j` since I do not like its numbering scheme.

## usage

Call with multiple files:

	unwrap-pdf-to-jpeg file.pdf other.pdf third.pdf

And you will end up with:

	file+1.jpg
	file+2.jpg
	file+3.jpg
	...
	file+8.jpg

	other+01.jpg
	...
	other+87.jpg

	third+1.jpg
	third+2.jpg
