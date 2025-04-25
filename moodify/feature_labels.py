import os, csv, time
import pandas as pd

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
client_id = "********************************"
client_secret = "********************************"

# Set up Spotify API client
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

def get_audio_features_in_batches(spotify, track_ids, batch_size=100):
    """Fetch audio features in batches of up to 100 track IDs."""
    audio_features = []
    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        audio_features.extend(spotify.audio_features(batch))
    return audio_features

def fetch_songs():
    start_time = time.time()
    playlist_id = "********************************"
    songs = []
    offset = 0
    
    while True:
        tracks = sp.playlist_tracks(playlist_id, offset=offset)
        if not tracks['items']:
            break
        songs.extend(tracks['items'])
        offset += len(tracks['items'])

    song_data = []
    song_ids = []

    for item in songs:
        track = item['track']
        song_id = track['id']
        song_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        duration_ms = track['duration_ms']

        song_data.append({
            'song_id': song_id,
            'name': song_name,
            'artist': artist_name,
            'album': album_name,
            'duration_ms': duration_ms,
            'custom_attributes': []
        })
        song_ids.append(song_id)

    audio_features_list = get_audio_features_in_batches(sp, song_ids)

    # Update song_data with audio features
    for i, audio_features in enumerate(audio_features_list):
        if audio_features:
            tempo = audio_features['tempo']
            danceability = audio_features['danceability']
            energy = audio_features['energy']
            valence = audio_features['valence']
            acousticness = audio_features['acousticness']
        else:
            tempo = danceability = energy = valence = acousticness = None

        song_data[i].update({
            'tempo': tempo,
            'danceability': danceability,
            'energy': energy,
            'valence': valence,
            'acousticness': acousticness
        })

    # Convert to a DataFrame and return
    df_songs = pd.DataFrame(song_data)
    end_time = time.time()
    print(f"fetch_songs() executed in {end_time - start_time:.2f} seconds")
    
    return df_songs

def add_attributes(df):
    for index, row in df.iterrows():
      print(f"\nCurrent song: {row['name']} by {row['artist']}")
      # Get the custom attributes from the user
      custom_attributes_input = input("Enter custom attributes (comma-separated, e.g., haunting, nostalgic): ")
      
      # Split the input string into a list and strip whitespace
      custom_attributes = [attr.strip() for attr in custom_attributes_input.split(',') if attr.strip()]
      
      # Update the DataFrame with the new attributes
      df.at[index, 'custom_attributes'] = custom_attributes
    return df

if __name__ == "__main__":
    df_songs = fetch_songs()
    df_songs = add_attributes(df_songs)
