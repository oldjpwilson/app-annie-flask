import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}

people = requests.get("https://www.appannie.com/en/about/leadership/", headers=headers)
print(people)

soup = BeautifulSoup(people.text, "html.parser")

divs = soup.find_all("div", {"class": "card_181czf1"})
# imgs = soup.find_all("p")

name_list = []

for d in divs:
    for name in d.find_all("h4"):
        n = name.text
    for title in d.find_all("p"):
        t = title.text
    name_list.append((n, t))


print(len(name_list), "\n", name_list)
