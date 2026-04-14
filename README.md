# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

your understanding of how real-world recommendations work and what your version will prioritize.

Explain your design in plain language:



Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Understanding of real-world recommendations:
  - Uses both collaborative (listeners with similar preferences' tastes) and content-based (song characteristics) data
  - Uses behavioral data, both explicit and implicit indicators of song preference: likes/dislikes (explicit), pressing the skip button (implicit), how long you listened before stopping (implicit)
  - Uses fancy machine learning algorithms for clustering song data of different listeners' together to recommend new songs based on other listeners' tastes (Matrix factorization, Deep Neural Networks)
  - Uses discrete features about audio-track's qualities-- genre, mood of song, valence(quantitative metric for mood), beats per minute, etc. 
    - Both subjective(danceability, mood, valence) and objective features(genre, beats per minute)
    - Used for tracking qualities and context of listening to song (when, what activity are users doing while listening, etc.)

My recommenders' System:
  - Scoring at high-level: Initial plan-- match to user-customizable "ideal profile". FUTURE: Allow for multiple distinct profiles, song suggestions based on matching to any one of them(most closely similar)
  - Content-based, collaboration-based, or hybrid: Initially, purely content-based
  - Songs.csv features to use for scoring songs, which UserProfile and Song will be matched on: energy, valence, danceability, acousticness, mood
  - Program flow at high-level: 
    - Inputs: number of songs to recommend, songs-data file, user-profile
    - Outputs: A list of songs
    - Takes csv of songs, and for each song, scores it based on how far it deviates from the 
    user-profile's preferences based on specific characteristics, and then ranks all of the songs in the data file and returns a list of only the top songs, the quantity is as-requested by the user
    - Characteristics of songs used for scoring: energy(fast-paced, vs calm), genre, mood (chill vs aggressive vs bubbly), and acoustic-level (instruments that sound non-electronic(ex. synths, beeps and boops))
     
  Scoring rule and then ranking rule to select the most relevant songs

  - Scoring rule: Weighted sum of differences, converted to match-score via formula (1/1+difference) with bonuses added to final match score. Differences-score calculated using energy and acoustic levels. The energy difference-score is 0.5 * abs(user_pref_energy - song_energy). Acousticness difference-score is 0.5 * weight, where weight is a decimal associated with a bin that the song is assigned based on its acoustic level and alignment with user-preference. Genre and mood are simple additive bonuses, where they provide a boost of 0.75 and 0.5 respectively to the match score if the exact match exists, but don't detract from the score if it doesn't. Genre provides marginally higher boost than mood, assuming we are creatures of habit and don't like large deviances from less flexible preferences like genre, initially.

  - Ranking rule: Simply order the songs in descending order, based on their match-score, and select the top X songs (X is an input to the program).
    
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---




## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

