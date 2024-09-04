import os 
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = os.path.join('..','config', 'client_secret.json')
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def create_youtube_service():
    print("Starting the OAuth flow for YouTube...")
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=8080)
    print("OAuth flow completed.")
    return build('youtube', 'v3', credentials=credentials)

def create_youtube_playlist(youtube, title, description):
    print(f"Creating YouTube playlist: {title}")
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["youtube", "playlist"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "public"
            }
        }
    )
    response = request.execute()
    print("Playlist created successfully.")
    return response['id']

def add_video_to_youtube_playlist(youtube, playlist_id, video_id):
    print(f"Adding video ID: {video_id} to playlist ID: {playlist_id}")
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"Added video ID: {video_id} to playlist ID: {playlist_id}")
