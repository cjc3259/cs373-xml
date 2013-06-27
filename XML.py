#!/usr/bin/env python

# ------------------------------
# projects/xml/RunXML.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

# ------------
# xml_read
# ------------

# from xml.etree.ElementTree import fromstring, ElementTree
from xml.etree import ElementTree
from xml.etree.ElementTree import fromstring
from cStringIO import StringIO


def xml_read (r, c) :
    """
    r is a list of strings of the remaining input by line
    c is a list of strings of the current case
    return true until EOF
    """
    if not r:
        return False

    i = 0
    while (not r[0].isspace()) :
        c.append(r[0])
        r.remove(c[i]) # removes the first element of r
        i += 1

        if not r:
            return True

    if r[0].isspace():
        space = r.pop(0)

    assert len(c) > 0
    return True


# ------------
# xml_eval
# ------------

def xml_eval (c, q) :
    """
    c is the current case as string
    q is the query as string
    returns a list of int's representing the output
    """
    # <your code>

    

# -------------
# xml_print
# -------------

def xml_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    # w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# xml_solve
# -------------

def xml_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    read_list = r.readlines() #list of strings by line
    # print len(read_list)
    case_list = []
    q_string = ''
    t_string = ''

    while xml_read (read_list, case_list) :
        q_string = case_list[len(case_list) - 1]
        case_list.pop()
        t_string = " ".join(case_list)
        print t_string
        print q_string
        xml_eval (t_string, q_string)
        # xml_print(w, a[0], a[1], v)
        # i = tree.getiterator()
        # print i
        case_list[:] = []