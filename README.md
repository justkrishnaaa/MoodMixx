# MoodMix - VibeViral

Welcome to **MoodMix**, a dynamic playlist generator that crafts personalized music experiences based on your mood! Inspired by the vibrant beats of Indian music (e.g., "Tu Jaane Na" for sad vibes, "Soni De Nakhre" for happy energy) and global hits, this project uses NLP sentiment analysis and the Spotify API to deliver 5 songs tailored to your emotions. With a sleek, aesthetic interface, it’s perfect for Gen Z music lovers seeking a "VibeViral" twist.

## Features
- **Mood Detection**: Analyzes your input (e.g., "I’m sad" or "Upbeat vibes!") using NLP to determine your mood.
- **Custom Playlists**: Generates 5 songs per mood (sad, happy, neutral, upbeat, bollywood) with Spotify tracks matching emotional criteria.
- **Aesthetic Design**: Features a gradient background, glassmorphism effects, and colorful buttons for a visually appealing experience.
- **Back Navigation**: Easy navigation with a back button on all pages.
- **Cross-Platform**: Runs locally via Flask and can be hosted with proper setup.

## Tech Stack
- **Python**: Core logic with Flask for the web app.
- **NLP**: Uses the `transformers` library (DistilBERT) for sentiment analysis.
- **Spotify API**: Fetches real-time tracks based on valence and energy.
- **HTML/CSS**: Bootstrap with custom CSS for styling.
- **GitHub**: Version control and deployment tracking.

## Prerequisites
- **Python 3.x**: Ensure Python is installed (`python --version`).
- **Virtual Environment**: Recommended for dependency management.
- **Spotify Developer Account**: For API access (get credentials at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)).
- **Libraries**: Install required packages:
  pip install flask transformers spotipy
  Installation


Clone the Repository:
Download or clone this repo to your local machine:



git clone https://github.com/yourusername/MoodMix.git
Or download the ZIP and extract it.
Set Up Virtual Environment:
Navigate to the project folder:



cd MoodMix
Create and activate a virtual environment:

python -m venv venv
nstall Dependencies:
Install the required libraries:



pip install -r requirements.txt
If requirements.txt doesn’t exist, manually run:



pip install flask transformers spotipy
Configure Spotify API:
Sign up at Spotify Developer Dashboard.
Create an app, note the Client ID and Client Secret.
Update src/main.py with your credentials:
python


spotify = SpotifyClient(client_id="your_client_id", client_secret="your_client_secret")
Add http://127.0.0.1:5000 as a Redirect URI in your app settings.
Run the App:
Start the server:



python src/main.py
Open your browser at http://127.0.0.1:5000 and enter a mood!









TEAM MEMBERS
KRISHNA THAKER-202407020397
KHUSHAL MATHUR-202407020393
JAIWARDHAN SINGH-202407020386