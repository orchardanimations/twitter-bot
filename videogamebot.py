import os
import logging
import random
from google import genai

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# ==========================================
# THE PROMPT VAULT
# ==========================================
PROMPT_LIST = [
    # --- POLITICAL EVENTS ---
    "Write a sharp, analytical tweet about the most significant political development from the past 24 hours. Keep it under 280 characters.",
    "Write a hot take on the latest Congressional or Parliamentary vote making headlines today. Keep it under 280 characters.",
    "Write a cynical tweet about the latest political scandal or controversy dominating the news cycle. Keep it under 280 characters.",
    "Write an insightful tweet analyzing the geopolitical implications of today's top international political story. Keep it under 280 characters.",
    "Write a tweet about the latest Supreme Court or major judicial decision and its broader societal impact. Keep it under 280 characters.",
    "Write a critical tweet about recent election results or polling data making waves. Keep it under 280 characters.",
    "Write a thought-provoking tweet on the latest foreign policy move by a major world power. Keep it under 280 characters.",
    "Write a tweet analyzing the political motivations behind today's most talked-about policy announcement. Keep it under 280 characters.",
    "Write a sharp tweet about the latest political figure making controversial headlines. Keep it under 280 characters.",
    "Write a tweet connecting today's political news to its historical context or precedent. Keep it under 280 characters.",

    # --- FINANCIAL MARKETS & ECONOMY ---
    "Write an analytical tweet about today's biggest stock market movement or trend. Keep it under 280 characters.",
    "Write a hot take on the latest Federal Reserve or central bank policy decision. Keep it under 280 characters.",
    "Write a tweet about the most significant corporate earnings report or business news from today. Keep it under 280 characters.",
    "Write a critical tweet analyzing today's inflation, employment, or major economic data release. Keep it under 280 characters.",
    "Write a tweet about the latest major merger, acquisition, or corporate restructuring making headlines. Keep it under 280 characters.",
    "Write an insightful tweet on today's currency market movements or foreign exchange developments. Keep it under 280 characters.",
    "Write a tweet about the latest housing market data or real estate trend in the news. Keep it under 280 characters.",
    "Write a sharp tweet analyzing the economic implications of today's top political or policy news. Keep it under 280 characters.",
    "Write a tweet about the latest tech sector development affecting markets. Keep it under 280 characters.",
    "Write a cynical tweet about the latest Wall Street scandal or financial regulatory news. Keep it under 280 characters.",

    # --- CRYPTO & BLOCKCHAIN ---
    "Write a tweet analyzing today's biggest cryptocurrency price movement and what's driving it. Keep it under 280 characters.",
    "Write a hot take on the latest crypto regulation or government crackdown making news. Keep it under 280 characters.",
    "Write a tweet about the most significant blockchain technology development announced today. Keep it under 280 characters.",
    "Write a critical tweet about the latest crypto exchange drama, hack, or controversy. Keep it under 280 characters.",
    "Write a tweet analyzing Bitcoin's current market position and what it signals. Keep it under 280 characters.",
    "Write an insightful tweet on the latest institutional adoption of crypto or blockchain. Keep it under 280 characters.",
    "Write a tweet about today's biggest NFT or Web3 news story. Keep it under 280 characters.",
    "Write a sharp tweet on the latest DeFi protocol exploit or vulnerability discovered. Keep it under 280 characters.",
    "Write a tweet about the latest major crypto company layoffs, bankruptcy, or restructuring. Keep it under 280 characters.",
    "Write a cynical tweet about the gap between crypto hype and reality based on today's news. Keep it under 280 characters.",

    # --- WORLD EVENTS & INTERNATIONAL NEWS ---
    "Write a tweet about the most significant breaking international news story from the past 24 hours. Keep it under 280 characters.",
    "Write an analytical tweet about the latest development in an ongoing global conflict or crisis. Keep it under 280 characters.",
    "Write a tweet about today's most impactful natural disaster, climate event, or environmental news. Keep it under 280 characters.",
    "Write a sharp tweet analyzing the latest UN, NATO, or major international organization decision. Keep it under 280 characters.",
    "Write a tweet about the latest major protest, social movement, or civil unrest making headlines. Keep it under 280 characters.",
    "Write an insightful tweet on today's most significant scientific breakthrough or research announcement. Keep it under 280 characters.",
    "Write a tweet about the latest major tech company announcement or product launch. Keep it under 280 characters.",
    "Write a critical tweet about today's most talked-about cultural or social controversy. Keep it under 280 characters.",
    "Write a tweet analyzing the latest space exploration or astronomical discovery in the news. Keep it under 280 characters.",
    "Write a tweet about the most significant public health or pandemic-related news from today. Keep it under 280 characters.",

    # --- CROSS-CATEGORY ANALYSIS ---
    "Write a tweet connecting today's political news to its market implications. Keep it under 280 characters.",
    "Write an analytical tweet about how today's crypto news reflects broader economic trends. Keep it under 280 characters.",
    "Write a tweet analyzing how today's geopolitical event will impact global markets. Keep it under 280 characters.",
    "Write a sharp tweet about the intersection of tech policy and market movements from today's news. Keep it under 280 characters.",
    "Write a tweet connecting today's economic data to political consequences. Keep it under 280 characters.",
    "Write an insightful tweet about how today's news fits into a larger historical or economic pattern. Keep it under 280 characters.",
    "Write a tweet about the most surprising or underreported story from today that deserves attention. Keep it under 280 characters.",
    "Write a contrarian take challenging the mainstream narrative about today's biggest news story. Keep it under 280 characters.",
    "Write a tweet predicting the second-order effects of today's major news event. Keep it under 280 characters.",
    "Write a tweet synthesizing the three most important news stories from today into a broader trend. Keep it under 280 characters."

    ]

def generate_tweet():
    # 1. Randomly select one prompt from the vault
    selected_prompt = random.choice(PROMPT_LIST)
    logging.info(f"Selected Prompt: {selected_prompt}")
    
    try:
        # 2. Feed the selected prompt to Gemini
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=selected_prompt,
        )
        tweet_text = response.text.strip()
        
        # 3. Trim to fit X's character limit just in case
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."
        return tweet_text
        
    except Exception as e:
        logging.error(f"Failed to generate tweet: {e}")
        return None

if __name__ == "__main__":
    logging.info("Waking up to generate new tweet text...")
    tweet = generate_tweet()
    
    if tweet:
        # Save the text directly to the file for the iPhone shortcut to read
        with open("latest_tweet.txt", "w", encoding="utf-8") as f:
            f.write(tweet)
        logging.info("Successfully saved to latest_tweet.txt")
