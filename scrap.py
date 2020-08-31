from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://books.toscrape.com/"
html = urlopen(url)

soup = BeautifulSoup(html,"html.parser")
type(soup)

all_links=str(soup.findAll('h3'))
clear= BeautifulSoup(all_links, "html.parser").get_text()
print(clear)
