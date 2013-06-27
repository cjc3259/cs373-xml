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

    ## setup tree structure for this case ##
    tree = ElementTree.parse(StringIO(c))
    tree_root = tree.getroot()
    tree_it = tree.getiterator()

    # assigns key values to all elements
    t_k = 1
    for i in tree_it:
        i.attrib['t_key'] = t_k
        t_k += 1

     # maps all elements to their parents
    tree_parent = dict((tc, tp) for tp in tree_it for tc in tp)


    ## setup tree structure for query ##
    query = ElementTree.parse(StringIO(q))
    query_root = query.getroot()
    query_it = query.getiterator()

    # maps all elements to their parents
    query_parent = dict((qc, qp) for qp in query_it for qc in qp)

    ## determine path from last element in query to root ##
    this_it = query_it[len(query_it) - 1]
    q_count = 0  # use this number to find output from tree
    for i in query_it:
        if this_it == query_it[0]:
            break
        this_it = query_parent[this_it]
        q_count += 1


    ## actual evaluation ##
    eval_list = tree.getroot().findall(XPath)
     
    output = [len(eval_list)]
    for i in range(len(eval_list)):
        output_key = 0
        output_it = eval_list[i]
        for j in range(q_count):
            output_it = tree_parent[output_it]
        output.append(output_it.get('t_key'))

    for i in output:
        print i
    
    return output
    

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