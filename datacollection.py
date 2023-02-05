import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


scopes = ['user-top-read', 'playlist-modify-public']

def login():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print ("Usage: %s username" % (sys.argv[0],))
        sys.exit()
    CLIENT_ID = '7339403e6dd34964b1e1c76fcafcc0be'
    CLIENT_SECRET = '37bfad7c0f7a4f14a29d6274a6735605'
    REDIRECT_URI = 'http://localhost:8888/callback'
    token = spotipy.util.prompt_for_user_token(
            username=username, scope=scopes, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, show_dialog = True)
    sp = spotipy.Spotify(auth=token)
    return sp
#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI,scope=scope))

def get_top_tracks(sp):
    results = sp.current_user_top_tracks(limit = 10, time_range='short_term')
    top_tracks = []
    for item in results['items']:
        artist = item['artists'][0]['name']
        track = item['name']
        print(track + " - " +artist)
        track_id = item['id']
        top_tracks.append(track_id)
    return top_tracks
        
def track_features(top_tracks, sp):
    track_id = []
    danceability = []
    energy = []
    loudness = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    track_name = []
    user = []
    results = sp.audio_features(top_tracks) 
    for item in results:
        user = sp.current_user()['display_name']
        track = sp.track(item['id'])
        track_name.append(track['name'])
        track_id.append(item['id'])
        danceability.append(item['danceability'])
        energy.append(item['energy'])
        loudness.append(item['loudness'])
        acousticness.append(item['acousticness'])
        instrumentalness.append(item['instrumentalness'])
        speechiness.append(item['speechiness'])
        liveness.append(item['liveness'])
        valence.append(item['valence'])
        tempo.append(item['tempo'])
    return user, track_id, track_name, danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo








# https://open.spotify.com/user/g7r4rw3do0x3qgxarzpvmf007?si=6e252c931a3a4699
# https://open.spotify.com/user/x885yw0xq6u87cfi4gxmv8eyn?si=112108c5d96741d6
# https://open.spotify.com/user/jeffisnotgay?si=abddf1f594ce44c1
# https://open.spotify.com/user/ym9tic7ghth7wa70fvi2eacpo?si=0de4136ad5474915 
# https://open.spotify.com/user/ldykbf2q50z5thi3wbyhxcw47?si=be92b1c253ec4e74