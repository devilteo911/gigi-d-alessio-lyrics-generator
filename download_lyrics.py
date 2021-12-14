# %% 

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# %% building the request and preparing the soup

URL: str = "https://www.lyricsmania.com/gigi_dalessio_lyrics.html"
URL_SONGS: str = "https://www.lyricsmania.com"
artist: str = "gigi_dalessio"

def soupify(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup

soup = soupify(URL)
# %% we grab all the artists' song links
songs_urls: list = []
for url in soup.find_all("a", title=True):
    subpage: str = url['href']
    html_ext = subpage[-5:]
    # I want to exclude non artists songs and other links
    if html_ext != ".html" or artist not in subpage:
        continue
    else:
        new_url: str = URL_SONGS + subpage
        songs_urls.append(new_url)

# %% we grab every artists' song text from links
with open("songs.csv", "w") as f:
    for url in tqdm(songs_urls):
        # I create the request and parse it with bs4
        soup = soupify(url)
        for div in soup.find_all("div",  attrs={'class':"lyrics-body"}):
                f.write(div.text)
                f.write(";")
f.close()



# %%
