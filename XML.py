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

    ## parse query into XPath ##
    XPath = './'

    traversed = []
    def parse(q_it):
        """
        takes a query element and parses the XML into an XPath for the associated element
        """

        this_XPath = '' 
        if q_it not in traversed:
            this_XPath += '/' + str(q_it.tag)
            traversed.append(q_it)

        # iterated through all the elements
        if len(traversed) == len(query_it):
            return this_XPath 

        children = q_it.getchildren()

        # if element has children
        if children:
            for i in children:
                if i not in traversed:
                    return this_XPath 
            return this_XPath + '/..'

        # if element does not have children
        else:
            return this_XPath + '/..' + parse(query_parent[q_it])

    # loop through all of the subelements in the query
    for i in query_it:
        XPath += parse(i)

    # print XPath

    ## actual evaluation ##
    eval_list = tree.getroot().findall(XPath)
     
    output = [len(eval_list)]
    for i in range(len(eval_list)):
        output_key = 0
        output_it = eval_list[i]
        for j in range(q_count):
            output_it = tree_parent[output_it]
        output.append(output_it.get('t_key'))
    
    return output
    
# -------------
# xml_print
# -------------

def xml_print (w, l) :
    """
    prints the values in output
    w is a writer
    """
    # w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
    for i in l:
        # print i
        w.write(str(i) + '\n')

    w.write('\n')
    # print w.getvalue()


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
    output = []

    while xml_read (read_list, case_list) :
        q_string = case_list[len(case_list) - 1]
        case_list.pop()
        t_string = " ".join(case_list)
        output = xml_eval (t_string, q_string)
        xml_print(w, output)
        case_list[:] = []

