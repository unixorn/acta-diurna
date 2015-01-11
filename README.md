# acta-diurna

Acta Diurna is a script to generate an motd file from a directory full of text
files and executables. It is modeled after update-motd on Amazon Linux, when
we switched to CentOS I missed having it.

Any files it finds in the directory that are not executables will be added to
the motd file verbatim, and any files that are executable will be run and
their output added to the motd file.
