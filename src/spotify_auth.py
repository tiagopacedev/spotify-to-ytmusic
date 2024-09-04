import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from the .env file
load_dotenv(os.path.join('..', 'config', '.env'))  


# Spotify credentials
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

# Set the scope to access playlists
scope = "playlist-read-private"

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=scope))
    return sp

def list_playlists(sp):
    playlists = sp.current_user_playlists()
    playlist_list = []

    
    for idx, playlist in enumerate(playlists['items']):
        print(f"{idx + 1}: {playlist['name']}")
        playlist_list.append((idx + 1, playlist['name'], playlist['id']))
    return playlist_list

def get_playlist_tracks(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
