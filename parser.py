from random import betavariate
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        list = ""
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            else:
                print("\n" + url)
                list += "{}\n".format(url)
            
            self.save(list)

    def save(self, url):
        with open("parsed.txt", "w") as file:
            file.write(url)

news = "https://news.sportbox.ru"
Scraper(news).scrape()