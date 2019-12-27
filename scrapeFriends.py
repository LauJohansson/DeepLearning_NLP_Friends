import requests
import pandas as pd
from bs4 import BeautifulSoup
import ftfy

session = requests.Session()

def makeSoup(url):
    res = session.get(url,timeout=5)
    res.raise_for_status()
    soup_content = BeautifulSoup(res.content, "lxml")
    for style in soup_content(["style"]):
        style.decompose()
    return soup_content

url = "https://fangj.github.io/friends/"
soup = makeSoup(url)

links = [url + link['href'] for link in soup.select("[href^='season']")]
results = [[link.split('season/')[1].split('.html')[0], makeSoup(link).select_one('html').text] for link in links]

df = pd.DataFrame(results)

for index, row in df.iterrows():
    with open('data/' + row[0] + '.txt', 'w', encoding='utf-8') as file:
        file.write(ftfy.fix_text(row[1]))