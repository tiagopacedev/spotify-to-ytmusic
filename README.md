# Spotify to YouTube Music - Playlist Transfer

This project allows you to transfer your playlists from Spotify to YouTube Music. It uses the Spotify and YouTube APIs to authenticate, retrieve playlists, and create new playlists on YouTube.

## Features

- Authenticate with Spotify and YouTube
- List Spotify playlists and liked songs
- Search for tracks on YouTube
- Create playlists on YouTube

## Prerequisites

- Python 3.6 or higher
- A Spotify Developer account
- A Google Developer account

## Setup

1. Create a virtual environment
```sh
python -m venv venv
```

2. Activate the virtual environment

- On Windows

  ```sh
  venv\Scripts\activate
  ```
  
- On macOS/Linux

  ```sh
  source venv/bin/activate
  ```

3. Install the required packages:
```sh
pip install -r requirements.txt
```

4. Create a .env file in the config directory and add your Spotify and YouTube API credentials:
```sh
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8080/
YOUTUBE_API_KEY=your_youtube_api_key
```

5. Create a client_secret.json file in the config directory with your Google API credentials.
