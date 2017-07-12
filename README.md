# Acta-Diurna

[![Code Climate](https://codeclimate.com/github/unixorn/acta-diurna/badges/gpa.svg)](https://codeclimate.com/github/unixorn/acta-diurna)
[![Issue Count](https://codeclimate.com/github/unixorn/acta-diurna/badges/issue_count.svg)](https://codeclimate.com/github/unixorn/acta-diurna)
[![Build Status](https://travis-ci.org/unixorn/acta-diurna.svg?branch=master)](https://travis-ci.org/unixorn/acta-diurna)
[![Join the chat at https://gitter.im/unixorn/acta-diurna](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/unixorn/acta-diurna?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![GitHub stars](https://img.shields.io/github/stars/unixorn/acta-diurna.svg)](https://github.com/unixorn/acta-diurna/stargazers)

Acta Diurna is a script to generate an motd file from a directory (`etc/update-motd.d` by default) full of text files and executables. I liked the functionality of update-motd on Amazon linux, and wanted something I could run on CentOS and OS X at work.

Any files acta-diurna finds in the update fragment directory tree that are not executables will be added to the motd file verbatim, and any files that are executable will be run and their output added to the motd file. Files & subdirectories are processed in alphanmeric order.

acta-diurna defaults to writing to `/etc/motd` and reading the update fragment files and scripts from `/etc/update-motd.d`.

The name is from the original Roman Acta Diurna or daily Roman official notices, and was chosen because I couldn't find another program with the same name.
