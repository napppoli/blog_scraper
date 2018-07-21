from bs4 import BeautifulSoup
import requests
import time

def get_body(filename,url):
    html = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(html.content, "lxml").find(id="days")
    date = soup.find(class_ = "date").string
    title = soup.find(class_="title").string
    print(date,title)
    body = soup.find(class_ = "section").get_text()
    with open(filename, 'a') as f:
        f.write('{} {}'.format(date,title))
        f.write(body+'\n')
