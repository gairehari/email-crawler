#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from lib import validate, find_emails


def main(args):
    '''Validate command line arguments.
       Use lib.find_emails library to find emails in a domain,
    '''
    if not validate.is_valid_domain(args.domain):
        print "Domain Name is not valid. Use valid domain name"
        sys.exit(1)

    d = find_emails.EmailsFromDomain(args.domain, args.protocol, args.maxpages)
    # d.find_all_emails()
    print d


if __name__ == "__main__":
    '''
    '''
    parser = argparse.ArgumentParser(description='Crawl emails \
                                     from a given domain.')

    parser.add_argument('domain',
                        help='domain name to fetch emails from')
    parser.add_argument('--protocol', default='http',
                        help='http/https')
    parser.add_argument('--maxpages', type=int, default=10,
                        help='maximum pages to be crawled')

    args = parser.parse_args()

    main(args)
