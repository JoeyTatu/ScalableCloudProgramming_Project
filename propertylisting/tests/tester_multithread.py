import requests
from multiprocessing.pool import Pool
from concurrent.futures import ThreadPoolExecutor
import importlib

from timer import timer

SampleUtilities = importlib.import_module('SampleUtilities')

URL = 'https://httpbin.org/uuid'

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