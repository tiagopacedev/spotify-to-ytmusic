import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from the .env file
load_dotenv(os.path.join('..', 'config', '.env'))  

# YouTube API key
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


def search_youtube(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    # Search for the query
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=1
    )
    response = request.execute()

    # Extract video IDs from the response
    video_ids = [item['id']['videoId'] for item in response['items']]
    return video_ids
