from ddgs import DDGS
from urllib.request import urlopen
import os

all_results = DDGS().text("wikipedia python", max_results = 1)
first_result = all_results[0]

print(all_results)

url = first_result['href']
print(f"URL: {url}")

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

with open("result.txt", "w") as file:
    file.write(html)