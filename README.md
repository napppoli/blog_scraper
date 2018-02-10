# blog_scraper
save your favorite blog posts onto local txt file

## Requirements
- Python 3.x
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](http://docs.python-requests.org/en/master/)

## How to use
For Hatena Diary:
```
python main.py -f <filename> -url <blog_url> -n <number_of_posts_to_save>
```
- filename: name of file to write the texts to.
- url: main URL of the target blog. ex) https://d.hatena.ne.jp/hoge/
- n: number of posts to save

Other blog service supports to be added soon...

