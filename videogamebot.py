import tweepy
import google.generativeai as genai
import time
import random
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# 1. Pull credentials securely from GitHub's environment variables
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_SECRET = os.environ.get("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# 2. Configure APIs
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') 

twitter_client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

def generate_tweet():
    prompt = (
        "Write a single, highly engaging tweet about video games, focusing strictly on "
        "either the Sonic the Hedgehog franchise or the Pokémon series. "
        "You can analyze game mechanics, in-game economies, world-building, lore, or focus on "
        "specific characters (like Tails). Make it a thought-provoking observation, a fun piece "
        "of trivia, or an interesting hot take. Do not use hashtags. Keep it under 280 characters."
    )
    
    try:
        response = model.generate_content(prompt)
        tweet_text = response.text.strip()
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."
        return tweet_text
    except Exception as e:
        logging.error(f"Failed to generate tweet: {e}")
        return None

def post_tweet(text):
    try:
        twitter_client.create_tweet(text=text)
        logging.info(f"Successfully posted: '{text}'")
    except Exception as e:
        logging.error(f"Failed to post tweet: {e}")

if __name__ == "__main__":
    # 3. Calculate random sleep to post at an unpredictable time during the hour
    # Random number between 0 and 59 minutes (3540 seconds)
    delay_seconds = # random.randint(0, 3540)
    delay_minutes = # delay_seconds / 60
    
    logging.info(f"GitHub Action triggered. Sleeping for {delay_minutes:.2f} minutes...")
    time.sleep(delay_seconds)
    
    # 4. Generate and post
    tweet = generate_tweet()
    if tweet:
        post_tweet(tweet)
