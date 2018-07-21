from bs4 import BeautifulSoup
import requests
import argparse
import time
from crawl import get_body
from next_node import get_url

parser = argparse.ArgumentParser(description='Save blog posts onto local .txt file')
parser.add_argument('--filename','-f',type=str,required=True,help='filename to save blog posts')
parser.add_argument('-url',required=True,type=str,help='URL of the blog starting with http://')
parser.add_argument('-n',type=int,default=100000,help='number of article to save')
args = parser.parse_args()

def main():
    filename = args.filename
    url = args.url
    suffix= '' if url[-1]=='/' else '/'
    url+=suffix+'archive'
    
    html = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(html.content, "lxml")
    url = soup.find("a", {"class","entry-title-link"}).get('href')
    n=args.n
    for i in range(n):
        get_body(filename,url)
        url=get_url(url)
    print('Successfully saved')

if __name__ == '__main__':
    main()
