#!/usr/bin/python

import getopt
import sys
# Our modules
import spamTest
import spamParse
import spamdb

def usage():
    print "-h,--help    Print this Help Message"
    print "-t,--train   Train on a message read from file"
    print "-f,--file=   The file to analyse"
    print ""
    print "The program will print out the spam value of an email"
    print "spaminess in order for a shell script to determine it."

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "htf:y", 
            ["help", "train", "file=", "yes"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)
        usage()
        sys.exit(2)
    # iterate over the prog args
    for o, a in opts:
        if o == "-t":
            training = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            fileName = a
        elif o in ("-y", "--yes"):
            isSpam = True
        else:
            assert False, "unhandled option"
    # begin program init
    spamdb.initSpamDb()

if __name__ == "__main__":
    main()
