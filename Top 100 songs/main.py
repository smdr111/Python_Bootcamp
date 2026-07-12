import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


#date = input(Which year do you want to travel to? Type the date in this format YYYY-MM-DD: )
TOP_SONGS_URL = f"https://appbrewery.github.io/bakeboard-hot-100/2021-05-15/"

response = requests.get(TOP_SONGS_URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data,'html.parser')
top_songs = [i.text for i in soup.find_all(name='h3',class_='chart-entry__title')]

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()


playlist_name = input('Name your playlist: ')
playlist_id = None

for p in playlists:
    if p["title"] ==  playlist_name:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        playlist_name,
        f"Playlist with the hottest songs",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")


for song in top_songs:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")























