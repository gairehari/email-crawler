
import re
import urllib2
import urlparse

from bs4 import BeautifulSoup

from lib.validate import EMAIL_RE


class EmailsFromDomain():

    def __init__(self, domain_name, https):
        '''
        '''
        self.domain_name = domain_name
        self.https = https
        self.emails = set()

        self.url = self.create_full_website_url()
        self.urls = [self.url]
        self.visited_urls = []

    def match_emails(self, text):
        '''Method to match and return emails in any given multiline text
        '''
        return list(set(re.findall(EMAIL_RE, text, re.I | re.M)))

    def create_full_website_url(self):
        '''Method to create full url from given domain name
        '''
        url = self.domain_name

        if self.https:
            url = 'https://' + url
        else:
            url = 'http://' + url

        return url

    def find_internal_links(self, url, response_text):
        '''Method to find all internal links in given domain
           If a link is already visited or doesn't contain given domain,
           it will not be visited.
        '''
        soup = BeautifulSoup(response_text, 'html.parser')
        for tag in soup.findAll('a', href=True):
            link = urlparse.urljoin(url, tag['href'])
            if not link:
                continue
            if (link not in self.visited_urls) and \
               (link not in self.urls) and \
               (self.domain_name in link):
                self.urls.append(link)

    def find_all_emails(self):
        '''Method to visit each link and find emails in them
        '''
        while self.urls:
            url = self.urls.pop()
            self.visited_urls.append(url)
            try:
                response = urllib2.urlopen(url)
            except Exception, e:
                #print url
                #print 'Exception fetching url content, %s' % str(e)
                continue  # URL not accessible

            data = response.read()

            emails = self.match_emails(data)
            if emails:
                self.emails.update(emails)

            self.find_internal_links(url, data)

    def get_emails(self):
        '''Returns list of emails found
        '''
        return list(self.emails)

    def __str__(self):
        '''Returns desired string representation of emails
        '''
        if self.emails:
            output = 'Found these email addresses:\n'
            for email in self.emails:
                output += email + '\n'
            return output.strip()
        else:
            return 'No Email addresses Found'
