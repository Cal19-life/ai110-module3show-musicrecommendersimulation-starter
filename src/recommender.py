from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"
    

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")

    songs: List[Dict] = []

    with open(csv_path, mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            try:
                song = {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            except (KeyError, TypeError, ValueError):
                # Skip malformed rows and continue parsing subsequent lines.
                continue

            songs.append(song)
            print(f"Successfully extracted {len(songs)} songs so far.")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    favorite_genre = user_prefs.get("favorite_genre", "")
    favorite_mood = user_prefs.get("favorite_mood", "")
    target_energy = float(user_prefs.get("target_energy", 0.5))
    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))

    energy = float(song.get("energy", 0.0))
    acousticness = float(song.get("acousticness", 0.0))

    # Agreed formula: 0.5 * absolute energy distance.
    energy_term = 0.5 * abs(energy - target_energy)

    # TODO: Adjust these acousticness thresholds to better match your desired bin boundaries.
    # TODO: Current cutoffs are heuristic defaults (0.25, 0.5, 0.75) and should be calibrated.
    # Agreed acoustic bin weights: best=0.0, closer-middle=0.45, farther-middle=0.55, worst=1.0.
    if likes_acoustic:
        if acousticness >= 0.75:
            acoustic_bin_weight = 0.0
            acoustic_label = "acoustic preference strongly aligned"
        elif acousticness <= 0.25:
            acoustic_bin_weight = 1.0
            acoustic_label = "acoustic preference strongly misaligned"
        elif acousticness >= 0.5:
            acoustic_bin_weight = 0.45
            acoustic_label = "acoustic preference moderately aligned"
        else:
            acoustic_bin_weight = 0.55
            acoustic_label = "acoustic preference mildly misaligned"
    else:
        if acousticness <= 0.25:
            acoustic_bin_weight = 0.0
            acoustic_label = "acoustic preference strongly aligned"
        elif acousticness >= 0.75:
            acoustic_bin_weight = 1.0
            acoustic_label = "acoustic preference strongly misaligned"
        elif acousticness < 0.5:
            acoustic_bin_weight = 0.45
            acoustic_label = "acoustic preference moderately aligned"
        else:
            acoustic_bin_weight = 0.55
            acoustic_label = "acoustic preference mildly misaligned"

    acoustic_term = 0.5 * acoustic_bin_weight

    total_distance = energy_term + acoustic_term
    base_match_score = 1.0 / (1.0 + total_distance)

    genre_bonus = 0.75 if song.get("genre", "") == favorite_genre else 0.0
    mood_bonus = 0.5 if song.get("mood", "") == favorite_mood else 0.0

    final_score = base_match_score + genre_bonus + mood_bonus

    reasons = [
        f"energy term={energy_term:.3f}",
        f"acoustic term={acoustic_term:.3f} ({acoustic_label})",
        f"base match={base_match_score:.3f}",
    ]
    if genre_bonus > 0:
        reasons.append("genre exact match bonus +0.75")
    if mood_bonus > 0:
        reasons.append("mood exact match bonus +0.50")

    return final_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
