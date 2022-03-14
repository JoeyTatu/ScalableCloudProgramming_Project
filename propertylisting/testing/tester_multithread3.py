#!/usr/bin/env python
import json
import ssl
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
import sys

#   examples https://stackoverflow.com/questions/16181121/a-very-simple-multithreading-parallel-url-fetching-without-queue
# see progress.md
urls = ["http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com"]

urls2 = ["https://10.5.164.210/api/siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&filter=status%%3D%%22OPEN%%22",
         "https://172.27.69.10/api/siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&filter=status%%3D%%22OPEN%%22"]


offenses_endpoint = 'siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&'
offenses_open_filter = 'filter=status%%3D%%22OPEN%%22'
domains_endpoint = 'config/domain_management/domains?fields=id,name'
notes_endpoint = 'siem/offenses/11781/notes'
headers1 = {'Accept': 'application/json', 'Content-Length': '0', 'sec': 'f4cfff1a-31e9-446d-8253-26f4005f53a0'}
headers2 = {'Accept': 'application/json', 'Content-Length': '0', 'sec': 'a61f06ce-71b4-4514-89b8-ddc49a9472cd'}

def fetch_url(url_request):


    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE


        response = urlopen(url_request , context=context)
        return url_request, response.read(), None
    except Exception as e:
        return url, None, e

start = timer()

server_ip1 = '10.5.164.210'
server_ip2 = '172.27.69.10'
base_uri = '/api/'
path_offenses =  offenses_endpoint+offenses_open_filter
headers1 = {'Accept': 'application/json', 'Content-Length': '0', 'sec': 'f4cfff1a-31e9-446d-8253-26f4005f53a0'}
headers2 = {'Accept': 'application/json', 'Content-Length': '0', 'sec': 'a61f06ce-71b4-4514-89b8-ddc49a9472cd'}
method = 'GET'


url1 = 'https://' + server_ip1 + base_uri + path_offenses

request1 = Request('https://' + server_ip1 + base_uri + path_offenses, headers=headers1)
request1.get_method = lambda: method

url2 = 'https://' + server_ip2 + base_uri + path_offenses

request2 = Request('https://' + server_ip2 + base_uri + path_offenses, headers=headers2)
request2.get_method = lambda: method

url_requests = [request1, request2]

'''
Threadpool Settings vs Elapsed Time 
20 = 26.97
30 = 25.96
40 = 24.74
50 = 25.83
'''

print(request1.origin_req_host)
print(request2.origin_req_host)

#results = ThreadPool(25).map(fetch_url, url_requests)
results = ThreadPool(40).imap_unordered(fetch_url, url_requests)
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
        #print(html)
        result = json.loads(html.decode("utf-8"))
        print(result)
    else:
        print("error fetching %r: %s" % (url, error))
print("Elapsed Time: %s" % (timer() - start,))
