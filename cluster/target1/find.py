from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys
argvs = sys.argv
argc = len(argvs)

html = urlopen("http://target_site.com/");
bsObj = BeautifulSoup(html.read(), "html.parser");
article = bsObj.find("div",{"class":"index_article_header_date"});
latesttime = article.find("time");
print("latesttime: ",latesttime.get_text());


article2 = bsObj.find("div",{"class":"index_article_header"}).find("h2");
urltag = article2.find("a");
if 'href' in urltag.attrs:
  url = urltag.attrs['href'];
  print("latest url: ",url);


