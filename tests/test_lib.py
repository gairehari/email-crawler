
import unittest

from lib import validate, find_emails


class FindEmailsTest(unittest.TestCase):

    def test_domain_name(self):
        assert validate.is_valid_domain('jana.com') is True
        assert validate.is_valid_domain('jana') is False

    def test_find_emails(self):
        ed = find_emails.EmailsFromDomain('', '')

        assert ed.match_emails('sales@jana.com') == ['sales@jana.com']
        assert ed.match_emails('jana') == []

if __name__ == '__main__':
    unittest.main()
