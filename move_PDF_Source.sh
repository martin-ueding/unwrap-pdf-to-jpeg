#!/bin/bash
# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

set -e
set -u

shopt -s nullglob

cd "$HOME/PDF_Source"

for c in {A..Z} {a..z} {0..9}
do
	files=$(echo ${c}*.*)

	if [[ -n "$files" ]]
	then
		echo "Folder $c"

		if [[ ! -d $c ]]
		then
			mkdir $c
		fi

		mv $files $c/
	fi
done
