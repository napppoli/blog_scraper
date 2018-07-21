from bs4 import BeautifulSoup
import requests
import argparse
import time
import os
from crawl import get_body
from next_node import get_url

parser = argparse.ArgumentParser(description = 'Save blog posts onto local .txt file')
parser.add_argument('-url',required = True, type = str,help = 'URL of the blog starting with http://')
parser.add_argument('-f', '--filename', type = str, default = 'saved_file', help = 'filename to save blog posts')
parser.add_argument('-n', type = int, default = 100000, help = 'number of article to save')
parser.add_argument('-t', type = str, default = 'txt', help = 'choose output file type. choices are txt or html')
args = parser.parse_args()

def main():
    filename = args.filename
    url = args.url
    suffix = '' if url[-1]=='/' else '/'
    url += suffix + 'archive'
    
    html = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(html.content, "lxml")
    url = soup.find("a", {"class","entry-title-link"}).get('href')
    n = args.n
    filetype = args.t
    if filetype == 'html':
        dir_name = url.split('.')[0].split('/')[-1]
        try:
            os.mkdir(dir_name)
        except:
            pass
    for i in range(n):
        get_body(filename, filetype, url)
        url = get_url(url)
    print('Successfully saved')

if __name__ == '__main__':
    main()
