#!/usr/bin/python

import spamdb
import getopt
import sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "htf:y", 
            ["help", "train", "file=", "yes"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-t":
            training = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...
