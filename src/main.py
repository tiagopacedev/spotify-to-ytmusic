from spotify_auth import authenticate_spotify, list_playlists, get_playlist_tracks
from youtube_auth import create_youtube_service, create_youtube_playlist, add_video_to_youtube_playlist
from youtube_search import search_youtube

if __name__ == "__main__":
    # Authenticate with Spotify
    sp = authenticate_spotify()
    
    print("Logging into Spotify...")
    
    # List user playlists
    playlist_list = list_playlists(sp)
    
    # Prompt user to select a playlist
    selected_idx = int(input("Enter the number of the playlist you want to transfer: ")) - 1
    
    selected_playlist_name = playlist_list[selected_idx][1]
    selected_playlist_id = playlist_list[selected_idx][2]
    print(f"You selected playlist: {selected_playlist_name} with ID: {selected_playlist_id}")
    
    # Get tracks from the selected playlist
    tracks = get_playlist_tracks(sp, selected_playlist_id)
    
    # Search each track on YouTube
    video_ids = []
    for idx, item in enumerate(tracks):
        track = item['track']
        query = f"{track['name']} by {track['artists'][0]['name']}"
        print(f"Searching YouTube for: {query}")
        video_id = search_youtube(query)
        if video_id:
            video_ids.append(video_id[0])
            print(f"Found YouTube track ID: {video_id[0]}")
        else:
            print(f"No YouTube track found for: {query}")

    # Log in to YouTube and create a service
    youtube = create_youtube_service()

    # Use the Spotify playlist name as the YouTube playlist title
    playlist_title = selected_playlist_name
    playlist_description = f"A playlist imported from Spotify: {playlist_title}"
    youtube_playlist_id = create_youtube_playlist(youtube, playlist_title, playlist_description)
    
    # Add each video ID to the new YouTube playlist
    for video_id in video_ids:
        add_video_to_youtube_playlist(youtube, youtube_playlist_id, video_id)

    # Print the link to the new YouTube playlist
    print(f"All videos added to the YouTube playlist '{playlist_title}'.")
    print(f"You can view your playlist here: https://music.youtube.com/playlist?list={youtube_playlist_id}")

