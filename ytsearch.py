
import requests
import random
from bs4 import BeautifulSoup


def ytsearch(query):
    url_endpoint = 'https://www.youtube.com/results'
    mydict = {'search_query': query}
    r = requests.get(url_endpoint, params=mydict)
    soup = BeautifulSoup(r.text, "html.parser")
    vids = []
    for vid in soup.find_all(attrs={"class": " yt-uix-sessionlink spf-link "}):
        if "results?search" not in vid['href']:
            vids.append('https://youtube.com' + vid['href'])
    return random.choice(vids)


    