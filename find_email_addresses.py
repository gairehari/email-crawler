#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from lib import check_domain, find_emails


def main():
    '''Main method to read command line arguments and validate them
       Uses lib.find_emails library to find emails in a domain
    '''
    args = sys.argv
    if len(args) < 2:
        print "Usage: python find_email_addresses.py valid_domain_name"
        return

    domain_name = args[1]
    if not check_domain.is_valid_domain(domain_name):
        print "Domain Name is not valid."
        print "Usage: python find_email_addresses.py valid_domain_name"
        return

    https = False
    if len(args) > 2:
        if args[2].lower() == 'https':
            https = True

    d = find_emails.EmailsFromDomain(domain_name, https)
    d.find_all_emails()
    print d


if __name__ == "__main__":
    main()
