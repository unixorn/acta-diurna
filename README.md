# Acta-Diurna

Acta Diurna is a script to generate an motd file from a directory full of text
files and executables. I liked the functionality of update-motd on Amazon
linux, and wanted something I could run on CentOS once we switched to it at
work.

Any files acta-diurna finds in the update fragment directory that are not
executables will be added to the motd file verbatim, and any files that are
executable will be run and their output added to the motd file.

acta-diurna defaults to writing to `/etc/motd` and reading the update fragment
files and scripts from `/etc/update-motd.d`

The name is from the original Roman Acta Diurna or daily Roman official
notices, and was chosen because there I couldn't find another program with the
same name.
