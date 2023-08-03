import pandas as pd
import numpy as np


album_names = input().split()
num = len(album_names)
release_years = input().split()
num_songs = input().split()
data = zip(album_names, release_years, num_songs)
df = pd.DataFrame(data, columns=["album_name", "release_year", "nsongs"], index=range(1, num + 1))
df = df.astype({"album_name": str,
                "release_year": int,
                "nsongs": int})
print(df)
