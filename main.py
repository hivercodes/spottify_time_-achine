import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#date = input("Please enter a time in the YYYY-MM-DD format:")

request = requests.get(f"https://www.billboard.com/charts/hot-100/2020-01-01/")

website = request.text

soup = BeautifulSoup(website, "html.parser")

data_list = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")

song_list = []

for l in data_list:
    song_list.append(l.text.replace("\t", "").replace("\n", ""))



auth_list = []

with open("../api/spotify") as auth:
    base_auth = auth.readlines()
    for inf in base_auth:
        auth_list.append(inf.strip("\n"))


oauth = {
    "client_id": auth_list[0],
    "client_secret": auth_list[1],
    "redirect_url": auth_list[2],
    "scope": "playlist-modify-private playlist-modify-public"
}


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=auth_list[2],
        client_id=auth_list[0],
        client_secret=auth_list[1],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]