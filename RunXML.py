#!/usr/bin/env python

# ------------------------------
# projects/xml/RunXML.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunXML.py < RunXML.in > RunXML.out
    % chmod ugo+x RunXML.py
    % RunXML.py < RunXML.in > RunXML.out

To document the program
    % pydoc -w XML
"""

# -------
# imports
# -------

import sys

from XML import xml_solve

# ----
# main
# ----

xml_solve(sys.stdin, sys.stdout)
