#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
def get_url(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "lxml").find(id="pager-top")
    ref = soup.a
    if ref['rel'][0] == 'prev':
        next = ref.get('href')
    else:
        print('Reached end of blog')
        sys.exit()
    prefix = 'http://d.hatena.ne.jp'
    return prefix+next