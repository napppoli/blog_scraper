#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
def get_url(url):
    html = requests.get(url)
    prefix = '/'.join(url.split('/')[:-1])
    soup = BeautifulSoup(html.content, "lxml")
    next_link = soup.find("a", {"class","skin-pagingNext skin-btnPaging ga-pagingEntryNextTop"})
    if isinstance(next_link, type(None)):
        print("Successfully reached end of the blog!")
        sys.exit()
    next = next_link["href"].split('/')[-1]
    return prefix+'/'+next
