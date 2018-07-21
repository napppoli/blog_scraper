from bs4 import BeautifulSoup
import requests
import time

def get_body(filename, filetype, url):
    html = requests.get(url)
    time.sleep(1)
    content=html.text.replace('<br />','\n')
    soup = BeautifulSoup(content, "lxml")
    date = soup.find("time").get("datetime")[:10]
    title = soup.find("a", {"class", "entry-title-link bookmark"}).string
    print(date,title)
    if filetype == 'html':
        dir_name = url.split('.')[0].split('/')[-1]
        with open('{}/{}.html'.format(dir_name,title), 'w') as f:
            f.write(html.text)
    else:
        body = soup.find("div",{"class", "entry-content"}).get_text()
        with open(filename, 'a') as f:
            f.write('{}\n{}\n'.format(date,title))
            f.write(body+'\n')
