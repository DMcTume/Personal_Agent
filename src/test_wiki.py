import os

import urllib.request
import json

#NOTE: spaces have to be converted to '_' in titles
titles = "Emu_War"

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + \
        titles + \
        "&formatversion=2&rvprop=content&rvslots=main"

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

data = None
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

with open("src/result.html", "w", encoding="utf-8") as file:
    file.write(data["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"])
    
