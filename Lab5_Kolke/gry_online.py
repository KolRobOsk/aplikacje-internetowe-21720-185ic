import requests
from bs4 import BeautifulSoup
while True:
    print("Wybierz stronę: \n1 - gry-online.pl\n2 - warhammerfantasy.fandom.com\n3 - pl.wikipedia.org")
    strona = input()
    if strona == "1":
        strona = "https://www.gry-online.pl"
        break
    elif strona == "2":
        strona = "https://warhammerfantasy.fandom.com/wiki/Warhammer_Wiki"
        break
    elif strona == "3":
        strona = "https://pl.wikipedia.org/wiki/Gra_fabularna"
        break
page = requests.get(strona)
soup = BeautifulSoup(page.content, "html.parser")
typ = input("Podaj typ do wyszukania: ")
all_tags = []
for element in soup.select(typ):
    all_tags.append(element.text)
print(all_tags)
