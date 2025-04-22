from flask import Flask, render_template, request
import os
from nlp_processor import analyze_mood
from spotify_client import SpotifyClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Spotify client
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify = SpotifyClient(client_id, client_secret)

@app.route("/", methods=["GET"])
def index():
    """Render the home page with the mood input form."""
    return render_template("index.html")

@app.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    """Process mood input and generate a playlist."""
    mood_description = request.form.get("mood")
    if not mood_description:
        return render_template("index.html", error="Please enter a mood description.")

    # Analyze mood
    mood, sentiment_score = analyze_mood(mood_description)

    # Get playlist
    playlist = spotify.get_playlist(mood)
    if not playlist:
        return render_template("index.html", error="Failed to generate playlist. Try again.")

    return render_template(
        "playlist.html",
        mood=mood,
        sentiment_score=round(sentiment_score, 2),
        playlist=playlist
    )

if __name__ == "__main__":
    app.run(debug=True)