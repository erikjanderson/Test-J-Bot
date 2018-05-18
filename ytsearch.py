
import requests
import random
from bs4 import BeautifulSoup


def ytsearch(query):
    r = requests.get("https://www.youtube.com/results?search_query=" + query)
    #print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    #print(soup)
    vids = []
    #g = soup.find_all(attrs={"class": "style-scope yt-img-shadow"})
    #print(g)
    for vid in soup.find_all(attrs={"class": " yt-uix-sessionlink spf-link "}):
        #print('got one')
        if "results?search" not in vid['href']:
            vids.append('https://youtube.com' + vid['href'])
    return random.choice(vids)


    