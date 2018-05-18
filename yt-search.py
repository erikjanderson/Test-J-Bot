import requests
from bs4 import BeautifulSoup

def searchYT(query):
    r = requests.get("https://www.youtube.com/results?search_query=")
    soup = BeautifulSoup(r.text, "html.parser")
    vids = []
    for vid in soup.find_all(attrs={"class": "style-scope yt-img-shadow"}):
        print('got one')
        vids.append('https://youtube.com' + vid['href'])
    return vids

x = searchYT('cat')
for i in x:
    print(i)