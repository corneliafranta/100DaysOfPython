import os
from pprint import pprint

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bs4 import BeautifulSoup


def ask_for_date():
    return input('From which date should the songs on your playlist be? Format: yyyy-mm-dd ')


date = ask_for_date()


def get_song_data():
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    response = requests.get(url)
    charts = response.text
    soup = BeautifulSoup(charts, 'html.parser')
    titles = [title.getText().strip('\n') for title in soup.find_all(name='h3', class_='a-no-trucate')]
    artists = [artist.getText().strip('\n') for artist in soup.find_all(name="span", class_="a-no-trucate")]
    return {'titles': titles, 'artists': artists}


spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri="http://example.com",
                              client_id=os.environ.get('CLIENT_ID'), client_secret=os.environ.get('CLIENT_SECRET'),
                              show_dialog=True,
                              cache_path="token.txt"))

user_id = spotify.current_user()['id']
song_data = get_song_data()


def get_song_uri(song, year):
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")
    else:
        return uri


uris = [get_song_uri(song, date.split('-')[0]) for song in song_data['titles']]
pprint(uris)

playlist = spotify.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public='false')

spotify.playlist_add_items(playlist_id=playlist['id'], items=uris)