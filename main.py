#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from crawl import get_body
from next_node import get_url
import argparse

parser = argparse.ArgumentParser(description='Save blog posts onto local .txt file')
parser.add_argument('--filename','-f',type=str,required=True,help='filename to save blog posts')
parser.add_argument('-url',required=True,type=str,help='URL of the blog starting with http://')
parser.add_argument('-n',type=int,default=100000,help='number of article to save')
args = parser.parse_args()
filename=args.filename
url = args.url
suffix= '' if url[-1]=='/' else '/'
url+=suffix+'archive'

html = requests.get(url)
soup = BeautifulSoup(html.content, "lxml").find(id="hatena-archive")
url = soup.find(class_ = "archive archive-date").find('a').get('href')

n=args.n
for i in range(n):
    get_body(filename,url)
    url=get_url(url)
    
print('Successfully saved')