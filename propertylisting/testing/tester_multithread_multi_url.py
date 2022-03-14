import requests
from multiprocessing.pool import Pool
from concurrent.futures import ThreadPoolExecutor
from timer import timer

from timer import timer

server_ip1 = '10.5.164.210'
sec1 = 'f4cfff1a-31e9-446d-8253-26f4005f53a0'

server_ip2 = '172.27.69.10'
sec2 = 'a61f06ce-71b4-4514-89b8-ddc49a9472cd'

base_uri = '/api/'
path = 'siem/offenses?fields=follow_up,inactive,assigned_to,id,domain_id,description,magnitude,credibility,relevance,severity,start_time,last_persisted_time&'

actual_headers = {'Accept': 'application/json', 'Content-Length': '0'}



request = Request(
    'https://' + self.server_ip + self.base_uri + path, headers=actual_headers
)

#response = session.get("https://kite.com", headers=session.headers)

def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

#   multithreading
@timer(1, 5)
def main():
    with ThreadPoolExecutor(max_workers=50) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 100, [URL] * 100)
            executor.shutdown(wait=True)


#   multiprocessing
'''
@timer(1, 1)
def main():
    with Pool() as pool:            #   allows asynch parrallel
        with requests.Session() as session:
            pool.starmap(fetch, [(session, URL) for _ in range(100)])
'''