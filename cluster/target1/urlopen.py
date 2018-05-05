from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys
import urllib.parse
argvs = sys.argv
argc = len(argvs)

# arg1  u:time update only else:posting
# arg2  filename: time file name

html = urlopen("http://target_site.com/");
bsObj = BeautifulSoup(html.read(), "html.parser");
article = bsObj.find("div",{"class":"index_article_header_date"});
latesttime = article.find("time");
print("latesttime: ",latesttime.get_text());

print(argc);
if argc == 3:
  filename = argvs[2];
else:
  filename = "timecheck";

try:
  f=open(filename, 'r');
  timecheck = f.read();
  print("stocktime : ",timecheck);
except FileNotFoundError:
  print("file does not exists. create.")
  f=open(filename, 'w');
  f.write("test");
  f.close();
  f=open(filename, 'r');
  timecheck = f.read();

#latest update check
if latesttime.get_text() != timecheck:
  print("time is different");
  f.close();
  f=open(filename,"w");
  f.write(latesttime.get_text());  
 
  article2 = bsObj.find("div",{"class":"index_article_header"}).find("h2");
  urltag = article2.find("a");
  if 'href' in urltag.attrs:
    url = urltag.attrs['href'];
    print("latest url: ",url); 
    _number = url.split("/");
    number = _number[4].split(".");
    a = number[0];
    print(a);
    #comment
    author_ = "名前
    comment_ = "メッセージ
    button_ = " 投稿する ";  

    author  = urllib.parse.urlencode({"author":author_.encode('euc-jp')});
    comment = urllib.parse.urlencode({"body":comment_.encode('euc-jp')});
    button  = urllib.parse.urlencode({"button":button_.encode('euc-jp')});         
    #post new commnet
    newcmd = "curl -H 'Host: target_site.com' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Origin: http://target_site.com' -H 'Upgrade-Insecure-Requests: 1' -A 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1)' -H 'Content-Type: application/x-www-form-urlencoded' -e 'http://target_site.com/archives/%s.html' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: ja,en-us;q=0.8,en;q=0.6' -X POST -d '%s' -d '%s' -d '%s' http://app.blog.livedoor.jp/target_site/comment.cgi/%s/post -o response" % (a, author, comment , button, a);
 
    #print(cmd);
    if argvs[1] == "u":
      print("# only update mode");
    else:
      print("# data has just post!!")
      print(newcmd);
      os.system(newcmd);

    sys.exit(2); 
else:
  print("time is same");
  #nothing to do
  sys.exit(5);
f.close();
