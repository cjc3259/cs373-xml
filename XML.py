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
        # print c[i]
        # print r[0]
        r.remove(c[i]) # removes the first element of r
        i += 1
        # print i
        if not r:
            return True

    if r[0].isspace():
        space = r.pop(0)

    assert len(c) > 0
    return True

# -------------
# xml_ElementTree
# -------------

# def xml_ElementTree (string_list):
#     """
#     c is a list of strings for this case by line
#     t is the XML ElementTree
#     q is the query ElementTree

#     """
#     # from xml.etree.ElementTree import fromstring

#     q_string = c[c.length - 1]
#     q = ElementTree(fromstring(q_string))
#     c.pop()
#     t_string = " ".join(c)
#     t = ElementTree(fromstring(t_string))
#     return t 


# ------------
# xml_eval
# ------------

def xml_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <your code>

    
    return v

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

    while xml_read (read_list, case_list) :
        q_string = case_list[len(case_list) - 1]
        print q_string
        query = ElementTree.parse(StringIO(q_string))
        case_list.pop()
        t_string = " ".join(case_list)
        print t_string
        tree = ElementTree.parse(StringIO(t_string))
        # xml_print(w, a[0], a[1], v)

        eval_list = tree.findall('.//Team/Cooly/../../JiaJia')
        # iterfind = tree.iterfind('.//Team/Cooly')
        # eval_list = tree.findall('/JiaJia/Team')
        # eval_list = tree.findall('./Cooly')
        print len(eval_list)
        # print eval_list[0].iter()
        # print iterfind
        case_list[:] = []
