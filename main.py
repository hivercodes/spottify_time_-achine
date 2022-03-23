import requests
from bs4 import BeautifulSoup


#date = input("Please enter a time in the YYYY-MM-DD format:")

request = requests.get(f"https://www.billboard.com/charts/hot-100/2020-01-01/")

website = request.text

soup = BeautifulSoup(website, "html.parser")

data_list = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")

song_list = []

for l in data_list:
    song_list.append(l.text.replace("\t", "").replace("\n", ""))


print(song_list)

