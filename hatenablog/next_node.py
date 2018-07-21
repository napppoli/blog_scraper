#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys

def get_url(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    ref = soup.find("span", class_="pager-next")
    if hasattr(ref,'a'):
        next = ref.a.get('href')
    else:
        print('Reached end of blog')
        sys.exit()
    return next
