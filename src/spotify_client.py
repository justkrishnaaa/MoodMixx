import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self, client_id, client_secret):
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        ))

    def get_playlist(self, mood, limit=10):
        mood_to_genre = {
            "sad": ["ballad", "acoustic", "blues"],
            "happy": ["pop", "dance", "funk"],
            "upbeat": ["upbeat", "pop", "dance", "funk"],
            "somber": ["somber", "blues", "classical", "acoustic"],
            "neutral": ["chill", "ambient", "lo-fi"],
            "bollywood": ["bollywood", "desi", "dance", "filmi", "indian-pop"]  # Refined genres for item songs
        }
        genre = mood_to_genre.get(mood.lower(), ["pop"])
        print(f"Fetching playlist for mood: {mood}, genres: {genre}")  # Debug print
        try:
            all_tracks = []
            for g in genre:
                results = self.client.search(q=f"genre:{g}", type="track", limit=limit // len(genre))
                tracks = results["tracks"]["items"]
                all_tracks.extend(tracks)
                print(f"Genre {g} returned {len(tracks)} tracks")  # Debug track count
            unique_tracks = list({track["id"]: track for track in all_tracks}.values())[:limit]
            print(f"Found {len(unique_tracks)} unique tracks after deduplication")  # Debug final count
            if not unique_tracks:
                print("No tracks found for the given genres. Consider adjusting genres.")
            playlist = [
                {
                    "name": track["name"],
                    "artist": track["artists"][0]["name"],
                    "url": track["external_urls"]["spotify"]
                }
                for track in unique_tracks
            ]
            for track in playlist:  # Debug track details
                print(f"Track: {track['name']} by {track['artist']}")
            return playlist
        except Exception as e:
            print(f"Error fetching playlist: {e}")
            return None