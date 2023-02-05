import datacollection 
import pandas as pd


def dataCollection():
    sp = datacollection.login()
    top_tracks = datacollection.get_top_tracks(sp)
    track_features = datacollection.track_features(top_tracks, sp)
    return track_features

def to_df():
    track_features_list = dataCollection()

    df_tracks = pd.DataFrame({'user': track_features_list[0], 'track_id':track_features_list[1], 'track_name':track_features_list[2],'danceability':track_features_list[3],
                            'energy':track_features_list[4], 'loudness':track_features_list[5], 'acousticness':track_features_list[6], 
                            'instrumentalness':track_features_list[7], 'liveness':track_features_list[8], 'valence':track_features_list[9], 'tempo':track_features_list[10]})
    print(df_tracks.shape)
    print(df_tracks.head(10))
    return df_tracks

from csv import writer 
from os.path import exists
def df_to_csv(df_tracks):
    filename = 'features.csv'
    file_exists = exists(filename) 
    if file_exists: 
        df_tracks.to_csv(filename,  header = False, mode = 'a')

    else:
        df_tracks.to_csv(filename, mode = 'w')
    return filename



