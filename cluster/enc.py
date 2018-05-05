import urllib.parse

parsed = urllib.parse.urlencode({"body":"日本語てすと".encode('euc-jp')});

print(parsed);

parsed2 = urllib.parse.urldecode(parsed);

print(parsed2);


