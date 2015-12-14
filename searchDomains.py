#!/usr/bin/env python
from publicsuffix import fetch, PublicSuffixList
import sys
import time
import argparse
import logging
import re

if __name__ == '__main__':

    #parse inputs files from stdin
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
    parser.add_argument('-v', '--verbose', action='store_const', const=logging.INFO, dest='loglevel',
                        help='increase output verbosity.')
    parser.add_argument('-d', '--debug', action='store_const', const=logging.DEBUG, dest='loglevel',
                        default=logging.WARNING, help='show debug output (even more than -v).')

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    #seperate two input files
    f1 =  args.file[0]
    f2 = args.file[1]

    #initialize dictionary and fetch public suffix list
    psl = PublicSuffixList(fetch())
    dictionary = {};

    #Grab domains from psl
    for line in f1.readlines():
        slvl = psl.get_public_suffix(line.strip())
        parts = re.split('\W+',slvl)
        dictionary[parts[0]] = 1
    
    #Check if word is in dictionary, if so print it
    for lines in f2.readlines():
        segments = re.split('\W+',lines)
        for name in segments:
            if dictionary.has_key(name):
                print lines 
                break 