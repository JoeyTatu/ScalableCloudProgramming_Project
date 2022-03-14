#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import quote
from urllib.request import Request
from urllib.request import urlopen
from urllib.request import install_opener
from urllib.request import build_opener
from urllib.request import HTTPSHandler


#   examples https://stackoverflow.com/questions/16181121/a-very-simple-multithreading-parallel-url-fetching-without-queue
# see progress.md
urls = [
    "http://www.google.com", 
    "http://www.apple.com", 
    "http://www.microsoft.com", 
    #"http://www.amazon.com", 
    "http://www.facebook.com"
    ]



def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e

start = timer()

results = ThreadPool(20).imap_unordered(fetch_url, urls)            #   TO DO try here to change the url to request object like in RestClient.py
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
    else:
        print("error fetching %r: %s" % (url, error))
print("Elapsed Time: %s" % (timer() - start,))