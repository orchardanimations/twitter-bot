import os
import logging
from google import genai

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Only Gemini is needed now!
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_tweet():
    prompt = (
        "Write a single, highly engaging tweet about video games, focusing strictly on "
        "either the Sonic the Hedgehog franchise or the Pokémon series. "
        "You can analyze game mechanics, in-game economies, world-building, lore, or focus on "
        "specific characters (like Tails). Make it a thought-provoking observation, a fun piece "
        "of trivia, or an interesting hot take. Do not use hashtags. Keep it under 280 characters."
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        tweet_text = response.text.strip()
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."
        return tweet_text
    except Exception as e:
        logging.error(f"Failed to generate tweet: {e}")
        return None

if __name__ == "__main__":
    logging.info("Generating new tweet text...")
    tweet = generate_tweet()
    
    if tweet:
        # Save the text directly to a file in the repository
        with open("latest_tweet.txt", "w", encoding="utf-8") as f:
            f.write(tweet)
        logging.info("Successfully saved to latest_tweet.txt")
