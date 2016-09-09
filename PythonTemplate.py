#!/usr/bin/env python

import io
import os
import re
import sys
from optparse import OptionParser
import subprocess

NAME = ""
VERBOSE = False
FILE = False

def run(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out

def parse(argv):
    global NAME, VERBOSE, FILE

    p = OptionParser(description="A Python template for the shell.",
                              prog="python {}".format(NAME),
                              version="0.1",
                              usage= "{} [option] [filename]".format(NAME))

    p.add_option("--verbose", "-v",
                action = "store_true",
                help="cause {} to be verbose, showing all \
                        operations".format(NAME),
                default=False)

    p.add_option("--file", "-f",
                action = "store_true",
                help="read from file",
                default=False)

    options, args = p.parse_args()
    if options.verbose:
        VERBOSE = True

def main(argc, argv):
    global NAME, FILE

    NAME = argv[0]
    parse(argv)

    f = io.open(argv[1], "r", encoding="utf8") if argc > 1 else sys.stdin
    for line in f:
        sys.stdout.write(line)

    f.close()
                

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
