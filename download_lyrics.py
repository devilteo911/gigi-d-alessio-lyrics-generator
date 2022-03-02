# %% 

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
from pathlib import Path

# %% building the request and preparing the soup

URL: str = "https://www.lyricsmania.com/gigi_dalessio_lyrics.html"
URL_SONGS: str = "https://www.lyricsmania.com"
# I create a folder to store all the songs
Path('dataset').mkdir(exist_ok=True)

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

for i, url in tqdm(enumerate(songs_urls), total=len(songs_urls)):
    if i == 60: break
    # To avoid IP ban
    if i % 20 == 0: time.sleep(5)
    # I create the request and parse it with bs4
    soup = soupify(url)
    for div in soup.find_all("div",  attrs={'class':"lyrics-body"}):       
        with open(f"dataset/songs_{i}.csv", "w") as f:
            f.write(div.text)
    # To avoid IP ban
    time.sleep(0.5)


# %%
