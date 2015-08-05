email-crawler
=======

A Python script to crawl emails from webpages in a given web domain.

Quick overview
--------------

```
Running Script

    python find_email_addresses.py domain_name

By Default, it assumes the given domain is in http.
To find emails in https domains, use:

    python find_email_addresses.py domain_name https

Example:

	python find_email_addresses.py harigaire.com
```

Libraries Required
------------------

BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)
It's included in the above library if you don't want to install it separately.