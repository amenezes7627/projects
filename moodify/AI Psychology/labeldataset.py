# Alison Menezes
# 05/20/2024
# v1
# file to label the dataset of known songs
# categories: comforting, creepy, bittersweet, floaty, runway, feelmyself, dancehype, emo, calming


import os, csv
import pandas as pd

music_directory = "C:/Users/music/Documents/music_dataset"

song_paths = [os.path.join(music_directory, f) for f in os.listdir(music_directory) if f.endswith('.mp3')]

labeled_songs = []
csv_path = "labeled_songs.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    
else:
    df = pd.DataFrame(columns=["file_path", "label"])
    for song in song_paths:
        print(f"Label: {song}")
        label = input("Enter the label (comforting, creepy, bittersweet, floaty, runway, feelmyself, dancehype, emo, calming, seductive, sweet): ")
        new_row = pd.DataFrame({"file_path": [song], "label": [label]})
        df = pd.concat([df, new_row], ignore_index=True)
        
    df.to_csv(csv_path, index=False)

