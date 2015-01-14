#!/usr/bin/env python2.7
#
# Copyright (C) 2015 Joe Block. All rights reserved.
#
# This program is released under the BSD 2-clause license. See LICENSE

"""
Acta Diurna is a script to generate an motd file from a directory full of text
files and executables.

Any files it finds in the directory that are not executables will be added to
the motd file verbatim, and any files that are executable will be run and their
output added to the motd file.

It defaults to writing to /etc/motd and reading the update fragments
from /etc/update-motd.d

"""

import argparse
import os
import subprocess


def is_executable(pathname):
  """Determine if a path is an executable file
  @param pathname: Path to examine
  """
  if os.path.isfile(pathname) and os.access(pathname, os.X_OK):
    return True
  return False


def generateMOTD(output='/etc/motd', updateDirectory='/etc/update-motd.d'):
  """Generate a MOTD file
  @param: output - file to write the motd to
  @param: updateDirectory - directory to search for fragment generators
  """
  motd = walkTree(updateDirectory)
  with open(output, "w") as motd_file:
    motd_file.write(motd)


def walkTree(updateDirectory='/etc/update-motd.d'):
  """Walk a directory tree and collect motd output.
  
  Executable files will be executed, and their output appended to the
  collected data; Regular files will have their contents appended, and
  subdirectories will be walked in turn. Files and subdirectories will be
  processed in alphanumeric order.

  @param: updateDirectory - directory to search for fragment generators.

  """

  motdData=""

  fragmentList = os.listdir(updateDirectory)
  fragmentList.sort()
  for cmd in fragmentList:
    commandPath = "%s/%s" % (updateDirectory, cmd)
    if os.path.isfile(commandPath):
      if is_executable(commandPath):
        motdData = motdData + subprocess.check_output(commandPath)
      else:
        with open(commandPath, 'r') as rawFile:
          motdData = motdData + rawFile.read()
    if os.path.isdir(commandPath):
      motdData = motdData + walkTree(commandPath)
  return motdData


def _getArgs():
  parser = argparse.ArgumentParser()
  parser.add_argument("--updateDirectory",
                      help="Specify directory to load fragment files from",
                      default="/etc/update-motd.d")
  parser.add_argument("--output",
                      help="Specify output file",
                      default="/etc/motd")
  return parser.parse_args()


if __name__ == "__main__":
  args = _getArgs()
  generateMOTD(output=args.output, updateDirectory=args.updateDirectory)
