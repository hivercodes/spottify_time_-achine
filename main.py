import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.parse
import json
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

#check if secret exists, if not ask for one
try:
    with open("token.txt") as token:
        token_list = list(token)
        token_dictionary = json.loads(token_list[0])
        secret = token_dictionary["access_token"]

except FileNotFoundError:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private playlist-modify-public",
            redirect_uri=auth_list[2],
            client_id=auth_list[0],
            client_secret=auth_list[1],
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]

#search peramiters
song_to_search = urllib.parse.quote(song_list[0])

song_search_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {secret}"
}


song_uri_list = []

#find uri and add to a list

#for song in song_list:
#    song_data = requests.get(url=f'https://api.spotify.com/v1/search?q={song_to_search}&type=track', headers=song_search_headers)
#    song_json = song_data.json()
#    song_uri = song_json["tracks"]["items"][0]["uri"]
#    song_uri_list.append(song_uri)




#create playlist

playlist_endpoint = f"https://api.spotify.com/v1/users/{auth_list[3]}/playlists"

