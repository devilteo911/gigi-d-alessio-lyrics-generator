# %% 

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# %% building the request and preparing the soup

URL = "https://www.lyricsmania.com/gigi_dalessio_lyrics.html"
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html.parser')

# %%

for url in soup.find_all("a", title=True):
    print(url)
# %%
