#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import argparse

def get_url(url,i):
    return url+str(i)+'.html'

def get_body(filename,url):
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    content=html.text.replace('<BR>','\n')
    soup = BeautifulSoup(content, "lxml")
    body = soup.get_text()
    with open(filename, 'a') as f:
        f.write('［＃改ページ］\n'+body+'\n')

parser = argparse.ArgumentParser(description='Save blog posts onto local .txt file')
parser.add_argument('--filename','-f',type=str,required=True,help='filename to save blog posts')
args = parser.parse_args()
filename=args.filename

url = 'http://www.geocities.jp/timeway/kougi-'

with open(filename, 'w') as f:
    f.write('世界史講義録\n')


n=135
for i in range(n):
    print('Scraping #{} lecture'.format(i))
    cur_url=get_url(url,i+1)
    print(cur_url)
    get_body(filename,cur_url)

print('Successfully saved')
