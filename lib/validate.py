
import re

DOMAIN_RE = r'^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$'
EMAIL_RE = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'


def is_valid_domain(domain_name):
    '''Method to validate if a given domain name is valid or not
    '''
    match = re.search(DOMAIN_RE, domain_name)
    if match:
        return True
    else:
        return False
