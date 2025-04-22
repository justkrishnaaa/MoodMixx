from transformers import pipeline

def analyze_mood(text):
    """
    Analyze the mood from user input using an emotion classification model.
    Returns a tuple of (mood, confidence_score).
    """
    # Load pre-trained emotion classification model
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    # Analyze emotion
    result = classifier(text, top_k=1)[0]
    emotion = result["label"]
    score = result["score"]

    # Map emotion to mood and genres
    mood_mapping = {
        "joy": ("upbeat", ["pop", "dance", "happy"]),
        "sadness": ("somber", ["blues", "acoustic", "sad"]),
        "anger": ("intense", ["rock", "metal", "punk"]),
        "fear": ("moody", ["ambient", "electronic"]),
        "surprise": ("energetic", ["dance", "electronic"]),
        "neutral": ("neutral", ["chill", "ambient"]),
        "disgust": ("dark", ["industrial", "alternative"])
    }

    mood, genres = mood_mapping.get(emotion, ("neutral", ["chill", "ambient"]))
    return mood, score