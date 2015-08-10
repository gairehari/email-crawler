email-crawler
=======

A Python script to crawl emails from webpages in a given web domain.

Quick overview
--------------

```
Running Script

    python find_email_addresses.py domain_name

Example:

	python find_email_addresses.py harigaire.com

By Default, it assumes the given domain has webpages in http. To find emails in https, use:

    python find_email_addresses.py domain_name --protocol https
```

Libraries Required
------------------

BeautifulSoup (http://www.crummy.com/software/BeautifulSoup/)

It's included in the above library if you don't want to install it separately.