#!/usr/bin/env python3

import time
import sys

import requests
import tinydb

def insert(url, path='db.json'):
    resp = requests.get(url).text
    try:
        title = resp.split('title>')[1][:-2]
    except:
        title = url
    db = tinydb.TinyDB(path)
    db.insert({'url': url, 'timestamp': str(int(time.time())), 'title': title})

def showall(path='db.json'):
    db = tinydb.TinyDB(path)
    url = tinydb.Query()
    return db.search(url['url'].test(lambda x: True))

def showdate(timestamp):
    return time.ctime(int(timestamp))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        for dicti in showall():
            print("{}\t{}\t{}".format(showdate(dicti['timestamp']), dicti['url'], dicti['title']))
    else:
        for url in sys.argv[1:]:
            insert(url)
