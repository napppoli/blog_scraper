#!/usr/bin/env python3
#coding: utf-8
from bs4 import BeautifulSoup
import requests
def get_body(filename,url):
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    content=html.text.replace('<br>','\n')
    soup = BeautifulSoup(content, "lxml")
    title = soup.find("a", {"class", "skinArticleTitle"}).text
    date = soup.find("time", {"class", "skin-textQuiet"}).text[:10]
    print('{} {}'.format(date,title))
    body = soup.find("div", {"class", "skin-entryBody"}).text
    with open(filename, 'a') as f:
        f.write('{}\n{}\n{}\n'.format(date,title,body))
