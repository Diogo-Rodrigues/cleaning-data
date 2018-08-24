# import pandas as pd
import pandas as pd

# read csv file
billboard = pd.read_csv('../datasets/billboard_lyrics_1964-2015.csv')

# Create the new DataFrame: tracks
tracks = billboard[['Rank', 'Year', 'Artist', 'Song', 'Lyrics',]]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())